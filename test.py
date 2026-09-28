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

    def test_not_integer(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        нецелого числа"""
        matrix = [[2.1, -3.3, 0, 0], [5, 2, -3, 0.7], [0, 5, 2, -3.2], [0, 0, 5, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_same_number_in_upper_diagonal(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, с непостоянными числами в наддиагонали"""
        matrix = [[2, -3, 0, 0], [5, 2, 1, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_same_number_in_main_diagonal(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, с непостоянными числами в главной диагонали"""
        matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 1, -3], [0, 0, 5, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_same_number_in_lower_diagonal(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, с непостоянными числами в поддиагонали"""
        matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 1, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_empty_rows_in_matrix(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, с пустыми вложенными списками"""
        matrix = [[], []]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_null_upper_diagonal(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, с постоянными нулевыми элементами в наддиагонали"""
        matrix = [[1, 0, 0], [-4, 1, 0], [0, -4, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_null_lower_diagonal(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, со постоянными нулевыми элементами в поддиагонали"""
        matrix = [[1, -2, 0], [0, 1, -2], [0, 0, 1]]
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

    def test_fifth_order(self):
        """Проверяет расчет определителя для матрицы порядка 5"""
        matrix = [
            [9, 8, 0, 0, 0],
            [7, 9, 8, 0, 0],
            [0, 7, 9, 8, 0],
            [0, 0, 7, 9, 8],
            [0, 0, 0, 7, 9],
        ]
        self.assertEqual(get_tridiagonal_determinant(matrix), -19575)

    def test_seventh_order(self):
        """Проверяет расчет определителя для матрицы порядка 7"""
        matrix = [
            [9, 8, 0, 0, 0, 0, 0],
            [7, 9, 8, 0, 0, 0, 0],
            [0, 7, 9, 8, 0, 0, 0],
            [0, 0, 7, 9, 8, 0, 0],
            [0, 0, 0, 7, 9, 8, 0],
            [0, 0, 0, 0, 7, 9, 8],
            [0, 0, 0, 0, 0, 7, 9],
        ]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1481769)


if __name__ == "__main__":
    unittest.main()
