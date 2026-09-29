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
                self.assertEqual(
                    calculate_determinant(test_case.matrix), test_case.det
                )

    def test_float_matrix(self):
        """Проверяет выброс исключения при наличии дробного числа в матрице"""
        matrix = [
            [1, 2, 3],
            [4, 42.21, 6],
            [7, 8, 9]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_int_float_numbers(self):
        """Проверяет корректность работы функции с целыми числами записанными как float"""
        matrix = [
            [1,2.0],
            [3.0,4]]
        self.assertEqual(calculate_determinant(matrix),-2)

    def test_zero_matrix(self):
        """Проверяет работу функции с нулевой матрицей"""
        matrix = [
            [0,0],
            [0,0]
        ]
        self.assertEqual(calculate_determinant(matrix),0)

    def test_double_empty_matrix(self):
        """Проверка исключения при пустой матрице с пустой строкой"""
        matrix = [[]]
        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_large_matrix(self):
        """Проверка работы при бОльших числах и более высоком порядке матрицы"""
        matrix = [
    [45, 12, 78, 34, 91, 23, 67, 89, 56, 11],
    [23, 89, 45, 67, 12, 34, 78, 91, 23, 56],
    [67, 34, 91, 12, 45, 78, 23, 56, 89, 11],
    [89, 56, 23, 78, 34, 11, 45, 12, 67, 91],
    [12, 78, 56, 91, 23, 67, 34, 45, 11, 89],
    [34, 45, 11, 23, 78, 89, 91, 67, 12, 56],
    [91, 67, 34, 56, 11, 45, 12, 78, 89, 23],
    [56, 23, 89, 45, 67, 12, 78, 34, 91, 11],
    [78, 11, 67, 89, 56, 91, 23, 12, 34, 45],
    [11, 91, 12, 34, 89, 56, 45, 23, 78, 67]
    ]
        self.assertEqual(calculate_determinant(matrix),-3250678692676237890)

    def test_minor_building(self):
        """Проверяет правильность построения миноров."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 10],
        ]

        self.assertEqual(calculate_determinant(matrix), -3)

    def test_transpose_same_determinant(self):
        """Проверяет, что транспонирование матрицы не изменяет её определитель."""
        matrix = [
            [2, -1, 3],
            [4, 5, 0],
            [7, 2, 6],
        ]

        transposed = [
            [2, 4, 7],
            [-1, 5, 2],
            [3, 0, 6],
        ]

        self.assertEqual(
            calculate_determinant(matrix),
            calculate_determinant(transposed),
        )

    def test_ragged_matrix(self):
        """Проверяет выброс исключения для матрицы со строками разной длины."""
        matrix = [
            [1, 2, 3],
            [4, 5],
            [6, 7, 8],
        ]

        self.assertRaises(Exception, calculate_determinant, matrix)


    def test_ragged_columns(self):
        """Проверяет выброс исключения для матрицы с неполными столбцами."""
        matrix = [
            [1],
            [2, 3],
            [4, 5, 6],
        ]

        self.assertRaises(Exception, calculate_determinant, matrix)

    def test_different_column_lengths(self):
        """Проверяет выброс исключения для матрицы со столбцами разной длины."""
        matrix = [
            [1, 2, 3, 4],
            [5, 6],
            [7, 8, 9],
        ]

        self.assertRaises(Exception, calculate_determinant, matrix)  
          
    def test_bool_matrix(self):
        """Проверяет, что функция выбрасывает исключение при наличии логических значений в матрице."""
        matrices = [
            [
                [1, True],
                [3, 4],
            ],
            [
                [1, 2],
                [False, 4],
            ],
        ]

        for matrix in matrices:
            with self.subTest(matrix=matrix):
                self.assertRaises(Exception, calculate_determinant, matrix)

if __name__ == "__main__":
    unittest.main()
