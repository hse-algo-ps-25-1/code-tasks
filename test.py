import unittest

from directed_cycle_error import DirectedCycleError
from main import topological_sort

GRAPH_TYPE_MESSAGE = "Граф задают списком списков целых номеров вершин"
VERTEX_RANGE_MESSAGE = "Номер вершины вне диапазона"


class TestTopologicalSort(unittest.TestCase):
    """Примеры топологической сортировки"""

    def test_single_vertex(self):
        """Одна вершина без дуг уже стоит в топологическом порядке"""
        self.assertEqual(topological_sort([[]]), [0])

    def test_chain(self):
        """Дуга ведёт от более ранней вершины результата к более поздней"""
        self.assertEqual(topological_sort([[1], []]), [0, 1])

    def test_cycle(self):
        """Ориентированный цикл не допускает топологической сортировки"""
        with self.assertRaisesRegex(
            DirectedCycleError, "В орграфе есть ориентированный цикл"
        ):
            topological_sort([[1], [0]])

    def test_not_a_list(self):
        """Орграф передают списком списков"""
        with self.assertRaisesRegex(
            TypeError, "Граф задают списком списков целых номеров вершин"
        ):
            topological_sort(None)

    def test_empty_graph(self):
        """Пустой орграф дает пустой порядок"""
        self.assertEqual(topological_sort([]), [])

    def test_reverse_indexed_chain(self):
        """Дуги цепочки идут от больших номеров к меньшим"""
        self.assertEqual(topological_sort([[], [0], [1], [2]]), [3, 2, 1, 0])

    def test_long_chain(self):
        """Длинная цепочка не упирается в предел глубины рекурсии"""
        vertex_count = 5000
        graph = [[vertex + 1] for vertex in range(vertex_count - 1)] + [[]]
        self.assertEqual(topological_sort(graph), list(range(vertex_count)))

    def test_chain_with_shortcuts(self):
        """Дуги из 0 в 1 и 2 сокращают цепочку 0, 3, 1, 2"""
        self.assertEqual(topological_sort([[1, 2, 3], [2], [], [1]]), [0, 3, 1, 2])

    def test_diamond_dag(self):
        """Две дуги ведут в одну вершину, верных порядков два"""
        self.assertIn(
            topological_sort([[1, 2], [3], [3], []]),
            ([0, 1, 2, 3], [0, 2, 1, 3]),
        )

    def test_input_graph_not_mutated(self):
        """Сортировка не меняет переданный орграф"""
        graph = [[1, 3, 2], [], [], []]
        topological_sort(graph)
        self.assertEqual(graph, [[1, 3, 2], [], [], []])

    def test_self_loop(self):
        """Петля образует ориентированный цикл"""
        self.assertRaises(DirectedCycleError, topological_sort, [[0]])

    def test_cycle_with_tail(self):
        """В цикл ведет дуга из вершины вне цикла"""
        self.assertRaises(DirectedCycleError, topological_sort, [[1], [2], [1]])

    def test_cycle_not_reachable_from_zero(self):
        """Цикл, до которого обход из вершины 0 не доходит"""
        self.assertRaises(DirectedCycleError, topological_sort, [[], [2], [1]])

    def test_tuple_graph(self):
        """Кортеж списков не считается списком списков"""
        self.assertRaisesRegex(
            TypeError, GRAPH_TYPE_MESSAGE, topological_sort, ([], [])
        )

    def test_tuple_neighbors(self):
        """Концы дуг вершины задают списком, а не кортежем"""
        self.assertRaisesRegex(
            TypeError, GRAPH_TYPE_MESSAGE, topological_sort, [(1,), []]
        )

    def test_vertex_not_an_int(self):
        """Номер вершины задают целым числом, 1.0 не подходит"""
        self.assertRaisesRegex(
            TypeError, GRAPH_TYPE_MESSAGE, topological_sort, [[1.0], []]
        )

    def test_bool_vertex(self):
        """Значение bool номером вершины не считается"""
        self.assertRaisesRegex(
            TypeError, GRAPH_TYPE_MESSAGE, topological_sort, [[True], []]
        )

    def test_negative_vertex_index(self):
        """Отрицательный номер вершины вне диапазона"""
        self.assertRaisesRegex(
            ValueError, VERTEX_RANGE_MESSAGE, topological_sort, [[], [-1]]
        )

    def test_vertex_index_equal_to_n(self):
        """Номер n уже вне диапазона от 0 до n - 1"""
        self.assertRaisesRegex(
            ValueError, VERTEX_RANGE_MESSAGE, topological_sort, [[2], []]
        )

    def test_type_checked_before_range(self):
        """Тип проверяется во всем графе раньше диапазона номеров"""
        self.assertRaisesRegex(
            TypeError, GRAPH_TYPE_MESSAGE, topological_sort, [[2], None]
        )

    def test_range_checked_before_cycle(self):
        """Номер вне диапазона замечается раньше цикла"""
        self.assertRaisesRegex(
            ValueError, VERTEX_RANGE_MESSAGE, topological_sort, [[0], [5]]
        )


if __name__ == "__main__":
    unittest.main()
