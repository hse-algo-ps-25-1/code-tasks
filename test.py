import unittest

from main import calculate_determinant
from matrix_generator import generate_matrix_and_det


def require_generator(test_case):
    sample = generate_matrix_and_det(1)
    if sample is None:
        test_case.skipTest("Generator is not implemented")
    return sample


class TestDeterminant(unittest.TestCase):
    """Набор тестов для проверки функции вычисления определителя
    целочисленной квадратной матрицы"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения None"""
        self.assertRaises(Exception, calculate_determinant, None)

    def test_matrix_must_be_a_list(self):
        """Проверяет тип внешнего контейнера матрицы."""
        invalid_matrices = (42, "matrix", ((1, 2), (3, 4)), ([1, 2], [3, 4]))
        for matrix in invalid_matrices:
            with self.subTest(matrix=matrix):
                self.assertRaises(Exception, calculate_determinant, matrix)

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, calculate_determinant, [])

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр прямоугольной матрицы"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [-4, 3, 5, -6]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_invalid_rows(self):
        """Проверяет строки неверного типа, пустые и рваные матрицы."""
        invalid_matrices = (
            [1],
            [[1, 2], (3, 4)],
            [[]],
            [[1, 2], [3]],
            [[1], [2]],
        )
        for matrix in invalid_matrices:
            with self.subTest(matrix=matrix):
                self.assertRaises(Exception, calculate_determinant, matrix)

    def test_elements_must_be_integers(self):
        """Проверяет, что каждый элемент матрицы является целым числом."""
        invalid_matrices = (
            [[1.0]],
            [["1"]],
            [[1, 2], [3, None]],
            [[True]],
        )
        for matrix in invalid_matrices:
            with self.subTest(matrix=matrix):
                self.assertRaises(Exception, calculate_determinant, matrix)

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        cases = (([[1]], 1), ([[0]], 0), ([[-7]], -7))
        for matrix, expected in cases:
            with self.subTest(matrix=matrix):
                self.assertEqual(calculate_determinant(matrix), expected)

    def test_second_order(self):
        """Проверяет расчет определителя для матрицы порядка 2"""
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(calculate_determinant(matrix), -2)

    def test_third_order(self):
        """Проверяет расчет определителя для матрицы порядка 3"""
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_fourth_order(self):
        """Проверяет расчет определителя для матрицы порядка 4"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [2, -5, -7, 5], [-4, 3, 5, -6]]
        self.assertEqual(calculate_determinant(matrix), 18)

    def test_zeroes_before_nonzero_expansion_element(self):
        """Проверяет знак дополнения не в первом столбце."""
        matrix = [[0, 0, 0, 2], [1, 0, 0, 0], [0, 3, 0, 0], [0, 0, 4, 0]]
        self.assertEqual(calculate_determinant(matrix), -24)

    def test_triangular_matrix(self):
        """Определитель треугольной матрицы равен произведению диагонали."""
        matrix = [
            [2, 5, -1, 3, 4],
            [0, -3, 4, 8, 1],
            [0, 0, 7, 2, -5],
            [0, 0, 0, -2, 6],
            [0, 0, 0, 0, 5],
        ]
        self.assertEqual(calculate_determinant(matrix), 420)

    def test_large_integer_elements(self):
        """Проверяет точный целочисленный результат для больших значений."""
        matrix = [[100_000, 2], [3, -100_000]]
        self.assertEqual(calculate_determinant(matrix), -10_000_000_006)

    def test_input_matrix_is_not_changed(self):
        """Проверяет, что вычисление не изменяет исходную матрицу."""
        matrix = [[2, -1, 3], [4, 0, 5], [-2, 1, 6]]
        original = [row.copy() for row in matrix]

        calculate_determinant(matrix)

        self.assertEqual(matrix, original)


class TestMatrixGenerator(unittest.TestCase):
    """Набор тестов генератора матриц с известным определителем."""

    def test_invalid_order(self):
        """Проверяет отклонение значений, не являющихся целым порядком >= 1."""
        require_generator(self)
        invalid_orders = (None, 0, -1, 1.5, "3", [], True)
        for order in invalid_orders:
            with self.subTest(order=order):
                self.assertRaises(Exception, generate_matrix_and_det, order)

    def test_generated_matrix_and_determinant(self):
        """Проверяет генератор матриц с известным определителем"""
        require_generator(self)
        for order in range(1, 11):
            with self.subTest(order=order):
                test_case = generate_matrix_and_det(order)
                self.assertEqual(len(test_case.matrix), order)
                for row in test_case.matrix:
                    self.assertIsInstance(row, list)
                    self.assertEqual(len(row), order)
                    for element in row:
                        self.assertIsInstance(element, int)
                self.assertIsInstance(test_case.det, int)
                self.assertEqual(calculate_determinant(test_case.matrix), test_case.det)


if __name__ == "__main__":
    unittest.main()
