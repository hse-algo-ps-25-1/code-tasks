import unittest
from collections.abc import Generator

from brute_force_tsp_solver import BruteForceTspSolver
from error_message_enum import ErrorMessageEnum
from permutation_generator import generate_permutations
from tsp_abs_solver import TspSolution


def assert_lex(test, elements, expected):
    """Генератор выдаёт перестановки в лексикографическом порядке"""
    result = generate_permutations(elements)
    test.assertIsInstance(result, Generator)
    test.assertEqual(list(result), expected)


class TestPermutationGenerator(unittest.TestCase):
    """Примеры генератора перестановок"""

    def test_empty(self):
        """Пустой список даёт одну пустую перестановку"""
        assert_lex(self, [], [[]])

    def test_single_num(self):
        """Один элемент даёт одну перестановку"""
        assert_lex(self, [1], [[1]])

    def test_double_num(self):
        """Два числа идут в лексикографическом порядке"""
        assert_lex(self, [2, 1], [[1, 2], [2, 1]])

    def test_three_num(self):
        """Три различных элемента дают шесть упорядоченных перестановок"""
        assert_lex(
            self,
            [8, 4, 6],
            [
                [4, 6, 8],
                [4, 8, 6],
                [6, 4, 8],
                [6, 8, 4],
                [8, 4, 6],
                [8, 6, 4],
            ],
        )

    def test_repeated(self):
        """Повторяющиеся элементы дают только различные перестановки"""
        assert_lex(
            self,
            [9, 5, 5],
            [[5, 5, 9], [5, 9, 5], [9, 5, 5]],
        )

    def test_wrong_type(self):
        """Строка вместо списка вызывает ошибку типа"""
        with self.assertRaises(TypeError):
            generate_permutations("789")

    def test_wrong_types_various(self):
        """Не список (в том числе bool, кортеж, int, None) даёт TypeError"""
        for invalid in [True, False, (1, 2), 123, None, {"a": 1}]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    generate_permutations(invalid)

    def test_strings_lexicographical(self):
        """Сравнимые строковые элементы упорядочиваются лексикографически"""
        assert_lex(
            self,
            ["c", "a", "b"],
            [
                ["a", "b", "c"],
                ["a", "c", "b"],
                ["b", "a", "c"],
                ["b", "c", "a"],
                ["c", "a", "b"],
                ["c", "b", "a"],
            ],
        )


class TestTsp(unittest.TestCase):
    """Примеры полного перебора коммивояжёра"""

    def test_not_a_list(self):
        """Орграф передают матрицей"""
        self.assertRaisesRegex(
            TypeError,
            ErrorMessageEnum.WRONG_MATRIX,
            BruteForceTspSolver,
            None,
        )

    def test_non_square_matrix(self):
        """Непрямоугольная матрица даёт TypeError"""
        matrix = [[None, 1.0, 2.0], [1.0, None]]
        self.assertRaisesRegex(
            TypeError,
            ErrorMessageEnum.WRONG_MATRIX,
            BruteForceTspSolver,
            matrix,
        )

    def test_invalid_matrix_element(self):
        """Матрица с нечисловыми значениями даёт TypeError"""
        matrix = [[None, "invalid"], [1.0, None]]
        self.assertRaisesRegex(
            TypeError,
            ErrorMessageEnum.WRONG_MATRIX,
            BruteForceTspSolver,
            matrix,
        )

    def test_negative_distance(self):
        """Отрицательное расстояние даёт ValueError"""
        matrix = [[None, -1.0], [1.0, None]]
        self.assertRaisesRegex(
            ValueError,
            ErrorMessageEnum.NEG_VALUE,
            BruteForceTspSolver,
            matrix,
        )

    def test_single(self):
        """Один город уже является маршрутом длины 0"""
        solver = BruteForceTspSolver([[None]])
        self.assertEqual(solver.get_tsp_solution(), TspSolution(0, [0]))

    def test_distance(self):
        """Длина маршрута — сумма последовательных рёбер"""
        matrix = [[None, 1.0], [2.0, None]]
        solver = BruteForceTspSolver(matrix)
        self.assertEqual(solver.get_distance(matrix, [0, 1, 0]), 3)
        self.assertEqual(solver.get_distance([[None]], [0]), 0)

    def test_distance_missing_edge(self):
        """Отсутствующее ребро в маршруте даёт расстояние None"""
        matrix = [[None, 1.0], [None, None]]
        solver = BruteForceTspSolver(matrix)
        self.assertIsNone(solver.get_distance(matrix, [0, 1, 0]))

    def test_double(self):
        """Два города: маршрут возвращается в начало"""
        matrix = [[None, 1.0], [2.0, None]]
        solver = BruteForceTspSolver(matrix)
        self.assertEqual(solver.get_tsp_solution(), TspSolution(3, [0, 1, 0]))

    def test_has_not_path(self):
        """Если цикла нет, расстояние пусто и маршрут пуст"""
        matrix = [[None, 1.0], [None, None]]
        solver = BruteForceTspSolver(matrix)
        self.assertEqual(solver.get_tsp_solution(), TspSolution(None, []))

    def test_zero_cycle(self):
        """Выбор кратчайшего цикла с нулевыми рёбрами"""
        matrix = [
            [None, 0, 8],
            [7, None, 0],
            [0, 6, None],
        ]
        solver = BruteForceTspSolver(matrix)
        self.assertEqual(
            solver.get_tsp_solution(),
            TspSolution(0, [0, 1, 2, 0]),
        )

    def test_shortest(self):
        """Из двух допустимых маршрутов выбирается кратчайший"""
        matrix = [
            [None, 5, 14],
            [11, None, 6],
            [8, 13, None],
        ]
        solver = BruteForceTspSolver(matrix)
        self.assertEqual(
            solver.get_tsp_solution(),
            TspSolution(19, [0, 1, 2, 0]),
        )

    def test_missing_edges(self):
        """При отсутствии части рёбер находится допустимый цикл"""
        matrix = [
            [None, 6, None],
            [None, None, 8],
            [7, None, None],
        ]
        solver = BruteForceTspSolver(matrix)
        self.assertEqual(
            solver.get_tsp_solution(),
            TspSolution(21, [0, 1, 2, 0]),
        )


if __name__ == "__main__":
    unittest.main()
