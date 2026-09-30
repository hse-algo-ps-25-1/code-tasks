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
        """Проверяет, что функция выбрасывает исключение при передаче None"""
        self.assertRaises(Exception, calculate_determinant, None)

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче пустого списка"""
        self.assertRaises(Exception, calculate_determinant, [])

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче прямоугольной матрицы"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [-4, 3, 5, -6]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_ragged_matrix(self):
        """Проверяет выброс исключения для «рваной» матрицы (строки разной длины)"""
        matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_matrix_with_empty_row(self):
        """Проверяет выброс исключения, если одна из строк пустая"""
        self.assertRaises(Exception, calculate_determinant, [[]])

    def test_not_a_list_type(self):
        """Проверяет передачу строк, чисел и кортежей вместо списков"""
        self.assertRaises(Exception, calculate_determinant, "not a matrix")
        self.assertRaises(Exception, calculate_determinant, 42)
        self.assertRaises(Exception, calculate_determinant, ((1, 2), (3, 4)))

    def test_contains_float(self):
        """Проверяет выброс исключения, если элементы имеют тип float"""
        matrix = [[1.0, 2], [3, 4]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_contains_bool(self):
        """Проверяет выброс исключения, если переданы bool (подкласс int в Python)"""
        matrix = [[True, False], [1, 0]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_contains_none_or_str_element(self):
        """Проверяет выброс исключения, если внутри есть None или строки"""
        self.assertRaises(Exception, calculate_determinant, [[1, "2"], [3, 4]])
        self.assertRaises(Exception, calculate_determinant, [[1, None], [3, 4]])

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        self.assertEqual(calculate_determinant([[1]]), 1)
        self.assertEqual(calculate_determinant([[-7]]), -7)
        self.assertEqual(calculate_determinant([[0]]), 0)

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
        matrix = [
            [3, -3, -5, 8],
            [-3, 2, 4, -6],
            [2, -5, -7, 5],
            [-4, 3, 5, -6],
        ]
        self.assertEqual(calculate_determinant(matrix), 18)

    def test_identity_matrix(self):
        """Определитель единичной матрицы любого порядка равен 1"""
        eye_3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(calculate_determinant(eye_3), 1)

    def test_zero_matrix(self):
        """Определитель матрицы из одних нулей равен 0"""
        zero_3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(calculate_determinant(zero_3), 0)

    def test_triangular_matrix(self):
        """Определитель треугольной матрицы равен произведению элементов главной диагонали"""
        upper_triangular = [[2, 3, 5], [0, 4, 7], [0, 0, 3]]
        # det = 2 * 4 * 3 = 24
        self.assertEqual(calculate_determinant(upper_triangular), 24)

    def test_generator(self):
        """Проверяет генератор матриц с известным определителем"""
        require_generator(self)
        for order in range(1, 11):
            with self.subTest(order=order):
                test_case = generate_matrix_and_det(order)
                self.assertEqual(len(test_case.matrix), order)
                for row in test_case.matrix:
                    self.assertEqual(len(row), order)
                self.assertEqual(calculate_determinant(test_case.matrix), test_case.det)


if __name__ == "__main__":
    unittest.main()
