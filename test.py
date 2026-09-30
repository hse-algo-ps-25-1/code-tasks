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

    def test_not_list(self):
        """Проверяет, что функция выбрасывает исключение при передаче в
        параметр значения, которое не является списком"""
        self.assertRaises(Exception, get_tridiagonal_determinant, 5)

    def test_rows_not_lists(self):
        """Проверяет, что функция выбрасывает исключение, если строки
        матрицы не являются списками"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [1, 2])

    def test_empty_row(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с пустой строкой"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [[]])

    def test_not_square_different_rows(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы, строки которой разной длины"""
        matrix = [[1, 2, 0], [3, 1], [0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_float_element(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с дробным элементом"""
        matrix = [[1.5, 2], [3, 1.5]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_string_element(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы со строковым элементом"""
        self.assertRaises(Exception, get_tridiagonal_determinant, [["1"]])

    def test_none_element(self):
        """Проверяет, что функция выбрасывает исключение при передаче
        матрицы с элементом None"""
        matrix = [[1, None], [3, 1]]
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
        
    def test_six_order(self):
        """Проверяет расчет определителя для матрицы порядка 6"""
        matrix = [[1,1,0,0,0,0], [1,1,1,0,0,0], [0,1,1,1,0,0], [0,0,1,1,1,0], [0,0,0,1,1,1], [0,0,0,0,1,1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1)

    def test_element_superdiagonal_equals_zero(self):
        """Проверяет расчет определителя матрицы при элементе наддиагонали равной нулю"""
        matrix = [[5,0,0], [2,5,0], [0,2,5]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 125)

    def test_element_supdiagonal_equals_zero(self):
        """Проверяет расчет определителя матрицы при элементе поддиагонали равной нулю"""
        matrix = [[3,1,0], [0,3,1], [0,0,3]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 27)

    def test_element_main_Diagonal_equals_zero_even(self):
        """Проверяет расчет определителя четной матрицы при элементе главной диагонали равной нулю"""
        matrix = [[0,4,0,0], [5,0,4,0], [0,5,0,4], [0,0,5,0]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 400)

    def test_element_main_Diagonal_equals_zero_odd(self):
        """Проверяет расчет определителя нечетной матрицы при элементе главной диагонали равной нулю"""
        matrix = [[0,4,0], [5,0,4], [0,5,0]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 0)

    def test_elements_superdiagonal_and_subdiagonal_equals_zero(self):
        """Проверяет расчет определителя матрицы при элементах наддиагонали и поддиагонали равных нулю"""
        matrix = [[2,0,0], [0,2,0], [0,0,2]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 8)

    def test_negative_elements_superdiagonal_and_subdiagonal(self):
        """Проверяет расчет определителя матрицы при негативных элементах наддиагонали и поддиагонали"""
        matrix = [[2,-1,0], [-3,2,-1], [0,-3,2]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -4)

    def test_not_zero_element_under_the_tape(self):
        """Проверяет, что функция выбрасывает исключение, если под лентой находится ненулевой элемент"""
        matrix = [[1,5,0,0], [2,1,5,0], [0,2,1,5], [7,0,2,1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_diff_element_main_Diagonal(self):
        """Проверяет, что на главной диагонали все элементы равны"""
        matrix = [[1,2,0], [3,4,2], [0,3,2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_diff_element_subdiagonal(self):
        """Проверяет, что элементы поддиагонали равны"""
        matrix = [[1,2,0], [5,1,2], [0,4,1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_diff_element_superdiagonal(self):
        """Проверяет, что элементы наддиагонали равны"""
        matrix = [[1,2,0], [5,1,3], [0,5,1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_tuple(self):
        """Проверяет, что на вход поступила матрица списком, а не кортежем"""
        matrix = [(1,2), (3,1)]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

if __name__ == "__main__":
    unittest.main()
