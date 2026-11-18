from enum import IntEnum
from queue import Queue

from unreachable_vertex_error import UnreachableVertexError


class VertexState(IntEnum):
    """Состояния вершины при обходе"""

    UNOPENED = 0
    OPEN = 1
    PROCESSED = 2


def _validate_graph(graph: list[list[int]]) -> None:
    if type(graph) is not list:
        raise TypeError("Граф задают списком списков целых номеров вершин")

    n = len(graph)

    for adj in graph:
        if type(adj) is not list:
            raise TypeError("Граф задают списком списков целых номеров вершин")
        for v in adj:
            if type(v) is not int:
                raise TypeError("Граф задают списком списков целых номеров вершин")
            if v < 0 or v >= n:
                raise ValueError("Номер вершины вне диапазона")


def _validate_vertex(vertex: int, n: int) -> None:
    if type(vertex) is not int:
        raise TypeError("Номер вершины должен быть целым числом")
    if vertex < 0 or vertex >= n:
        raise ValueError("Номер вершины вне диапазона")


def _build_path(parent: list[int | None], goal: int) -> list[int]:
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path


def shortest_path(graph: list[list[int]], start: int, goal: int) -> list[int]:
    """Возвращает кратчайший по числу рёбер путь из start в goal.

    graph — список списков. Вершины — индексы 0, 1, ..., n - 1.
    graph[i] — концы дуг, выходящих из i. Путь содержит start и goal.
    При start == goal путь состоит из одной вершины. Списки смежности
    при этом всё равно проверяются.

    :param graph: списки смежности орграфа
    :param start: номер начальной вершины
    :param goal: номер конечной вершины
    :raises TypeError: Граф задают списком списков целых номеров вершин
    :raises TypeError: Номер вершины должен быть целым числом
    :raises ValueError: Номер вершины вне диапазона
    :raises UnreachableVertexError: Вершина недостижима
    :return: вершины кратчайшего пути
    """
    _validate_graph(graph)
    n = len(graph)
    _validate_vertex(start, n)
    _validate_vertex(goal, n)

    if start == goal:
        return [start]

    state = [VertexState.UNOPENED] * n
    parent = [None] * n

    queue = Queue()
    state[start] = VertexState.OPEN
    queue.enqueue(start)

    while not queue.is_empty():
        u = queue.dequeue()
        for v in graph[u]:
            if state[v] == VertexState.UNOPENED:
                state[v] = VertexState.OPEN
                parent[v] = u
                if v == goal:
                    return _build_path(parent, goal)
                queue.enqueue(v)
        state[u] = VertexState.PROCESSED

    raise UnreachableVertexError()


def main():
    print(shortest_path([[1], []], 0, 1))


if __name__ == "__main__":
    main()
