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

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, calculate_determinant, [])

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр прямоугольной матрицы"""
        matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [-4, 3, 5, -6]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        matrix = [[1]]
        self.assertEqual(calculate_determinant(matrix), 1)

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

    def test_not_list(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        в параметр значение, которое не является списком"""
        self.assertRaises(Exception, calculate_determinant, 123)

    def test_not_matrix_string(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        в параметр строки"""
        self.assertRaises(Exception, calculate_determinant, "abc")

    def test_row_not_list(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        в параметр матрицу,
        которая состоит не только из списков"""
        matrix = [[1, 2], (3, 4)]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_dif_row_len(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        в параметр матрицу,
        имееющую строки разной длины"""
        matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_float(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        в параметр матрицу,
        которая имеет в себе вещественное число"""
        matrix = [[1, 2, 3], [4, 5, 8.5], [6, 7, 8]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_string(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        в параметр матрицу, которая имеет в себе строчный элемент"""
        matrix = [[1, 2, 3], [4, 5, 8.5], [6, 7, 8]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_zero_first_order(self):
        """Проверяет матрицу порядка 1 со значением 0"""
        matrix = [[0]]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_negative_first_order(self):
        """Проверяет матрицу порядка 1 со значением -7"""
        matrix = [[-7]]
        self.assertEqual(calculate_determinant(matrix), -7)

    def test_identity_matrix(self):
        """Проверяет единичную матрицу"""
        matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(calculate_determinant(matrix), 1)

    def test_negative_matrix(self):
        """Проверяет матрицу с отрицательными числами"""
        matrix = [[-1, -2, -5], [-10, -50, -2], [-11, -58, -10]]
        self.assertEqual(calculate_determinant(matrix), -378)

    def test_fifth_order(self):
        """Проверяет расчет определителя для матрицы порядка 5"""
        matrix = [
            [2, 1, 3, 4, 5],
            [0, 3, 2, 1, 4],
            [0, 0, 4, 2, 3],
            [0, 0, 0, 5, 1],
            [0, 0, 0, 0, 6],
        ]
        self.assertEqual(calculate_determinant(matrix), 720)


if __name__ == "__main__":
    unittest.main()
