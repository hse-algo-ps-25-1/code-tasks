import unittest

from main import shortest_path
from unreachable_vertex_error import UnreachableVertexError


class TestShortestPath(unittest.TestCase):
    """Примеры кратчайшего пути"""

    def test_same_vertex(self):
        """Путь из вершины в неё саму не содержит рёбер"""
        self.assertEqual(shortest_path([[0]], 0, 0), [0])

    def test_one_edge(self):
        """Единственная дуга и есть кратчайший путь"""
        self.assertEqual(shortest_path([[1], []], 0, 1), [0, 1])

    def test_shortest_of_two_paths(self):
        """Выбирается кратчайший по числу рёбер путь"""
        graph = [[1, 2], [2], [3], []]
        self.assertEqual(shortest_path(graph, 0, 3), [0, 2, 3])

    def test_graph_with_cycle(self):
        """Обход корректно работает в графе с циклом"""
        graph = [[1], [0, 2], [3], []]
        self.assertEqual(shortest_path(graph, 0, 3), [0, 1, 2, 3])

    def test_unreachable_vertex(self):
        """Ошибка при отсутствии пути"""
        with self.assertRaisesRegex(UnreachableVertexError, "Вершина недостижима"):
            shortest_path([[1], [], [0]], 0, 2)

    def test_not_a_list(self):
        """Орграф передают списком списков"""
        with self.assertRaisesRegex(
            TypeError, "Граф задают списком списков целых номеров вершин"
        ):
            shortest_path(None, 0, 0)

    def test_row_not_a_list(self):
        """Элемент графа не является списком"""
        with self.assertRaisesRegex(
            TypeError, "Граф задают списком списков целых номеров вершин"
        ):
            shortest_path([0], 0, 0)

    def test_bool_in_adj_list(self):
        """Значение bool в списке смежности не считается целым номером"""
        with self.assertRaisesRegex(
            TypeError, "Граф задают списком списков целых номеров вершин"
        ):
            shortest_path([[True]], 0, 0)

    def test_adj_vertex_out_of_range(self):
        """Сосед в списке смежности вне диапазона"""
        with self.assertRaisesRegex(ValueError, "Номер вершины вне диапазона"):
            shortest_path([[2], []], 0, 0)

    def test_start_or_goal_not_int(self):
        """Номера начальной и конечной вершин должны быть целыми"""
        with self.assertRaisesRegex(
            TypeError, "Номер вершины должен быть целым числом"
        ):
            shortest_path([[0]], True, 0)
        with self.assertRaisesRegex(
            TypeError, "Номер вершины должен быть целым числом"
        ):
            shortest_path([[0]], 0, "0")

    def test_start_or_goal_out_of_range(self):
        """Номера начальной и конечной вершин вне диапазона"""
        with self.assertRaisesRegex(ValueError, "Номер вершины вне диапазона"):
            shortest_path([[0]], -1, 0)
        with self.assertRaisesRegex(ValueError, "Номер вершины вне диапазона"):
            shortest_path([[0]], 0, 1)


if __name__ == "__main__":
    unittest.main()
