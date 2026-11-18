from enum import IntEnum

from directed_cycle_error import DirectedCycleError
from stack import Stack

GRAPH_TYPE_MESSAGE = "Граф задают списком списков целых номеров вершин"
VERTEX_RANGE_MESSAGE = "Номер вершины вне диапазона"


class VertexState(IntEnum):
    """Состояния вершины при обходе"""

    UNOPENED = 0
    OPEN = 1
    PROCESSED = 2


def topological_sort(graph: list[list[int]]) -> list[int]:
    """Возвращает вершины орграфа в топологическом порядке.

    graph — список списков. Вершины — индексы 0, 1, ..., n - 1.
    graph[i] — концы дуг, выходящих из i. Результат содержит каждую вершину
    один раз, и начало каждой дуги стоит в нём раньше конца.

    :param graph: списки смежности орграфа
    :raises TypeError: Граф задают списком списков целых номеров вершин
    :raises ValueError: Номер вершины вне диапазона
    :return: номера вершин в топологическом порядке
    """
    validate_graph(graph)
    states = [VertexState.UNOPENED] * len(graph)
    processed_order = []
    open_vertices = Stack()

    for start in range(len(graph)):
        if states[start] != VertexState.UNOPENED:
            continue
        states[start] = VertexState.OPEN
        open_vertices.push((start, iter(graph[start])))

        while not open_vertices.is_empty():
            vertex, unchecked_neighbors = open_vertices.peek()
            neighbor = next(unchecked_neighbors, None)
            if neighbor is None:
                open_vertices.pop()
                states[vertex] = VertexState.PROCESSED
                processed_order.append(vertex)
            elif states[neighbor] == VertexState.OPEN:
                raise DirectedCycleError()
            elif states[neighbor] == VertexState.UNOPENED:
                states[neighbor] = VertexState.OPEN
                open_vertices.push((neighbor, iter(graph[neighbor])))

    return processed_order[::-1]


def validate_graph(graph: list[list[int]]) -> None:
    """Проверяет формат списков смежности и диапазон номеров вершин."""
    if not isinstance(graph, list):
        raise TypeError(GRAPH_TYPE_MESSAGE)
    for neighbors in graph:
        if not isinstance(neighbors, list):
            raise TypeError(GRAPH_TYPE_MESSAGE)
        for vertex in neighbors:
            if not isinstance(vertex, int) or isinstance(vertex, bool):
                raise TypeError(GRAPH_TYPE_MESSAGE)
    for neighbors in graph:
        for vertex in neighbors:
            if not 0 <= vertex < len(graph):
                raise ValueError(VERTEX_RANGE_MESSAGE)


def main():
    print(topological_sort([[1], []]))


if __name__ == "__main__":
    main()
