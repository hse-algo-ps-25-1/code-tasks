import unittest

from main import get_tridiagonal_determinant


class TestTridiagonalDeterminant(unittest.TestCase):
    """Набор тестов для проверки функции вычисления определителя
    трёхдиагональной ленточной матрицы"""

    def test_none(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения None"""
        self.assertRaises(Exception, get_tridiagonal_determinant, None)

    def test_empty_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр пустого списка"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [])

    def test_not_square_rectangle(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр прямоугольной матрицы"""
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_zero(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с ненулевым элементом вне трёх диагоналей"""
        matrix = [[1, 2, 0, 7], [3, 1, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_first_order(self):
        """Проверяет расчет определителя для матрицы порядка 1"""
        matrix = [[1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1)

    def test_second_order(self):
        """Проверяет расчет определителя для матрицы порядка 2"""
        matrix = [[1, 2], [2, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -3)

    def test_third_order(self):
        """Проверяет расчет определителя для матрицы порядка 3"""
        matrix = [[1, -2, 0], [-4, 1, -2], [0, -4, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -15)

    def test_fourth_order(self):
        """Проверяет расчет определителя для матрицы порядка 4"""
        matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 421)

    def test_main_diagonal_is_not_constant(self):
        """Проверяет, что главная диагональ не является постоянной"""
        matrix = [[6, 2, 0], [3, 7, 2], [0, 3, 9]]
        self.assertRaises(ValueError, get_tridiagonal_determinant, matrix)

    def test_upper_diagonal_is_not_constant(self):
        """Проверяет, что наддиагональ не является постоянной"""
        matrix = [[6, 7, 0], [3, 9, 6], [0, 3, 7]]
        self.assertRaises(ValueError, get_tridiagonal_determinant, matrix)

    def test_lower_diagonal_is_not_constant(self):
        """Проверяет, что поддиагональ не является постоянной"""
        matrix = [[9, 6, 0], [7, 9, 6], [0, 6, 9]]
        self.assertRaises(ValueError, get_tridiagonal_determinant, matrix)


if __name__ == "__main__":
    unittest.main()
