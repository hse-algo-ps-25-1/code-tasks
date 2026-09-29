import unittest

from main import get_tridiagonal_determinant


class TestTridiagonalDeterminant(unittest.TestCase):
    def test_none(self):
        self.assertRaises(Exception, get_tridiagonal_determinant, None)

    def test_empty_matrix(self):
        self.assertRaises(Exception, get_tridiagonal_determinant, [])

    def test_not_square_rectangle(self):
        matrix = [[1, 2, 0, 0], [3, 1, 2, 0], [0, 3, 1, 2]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_not_tridiag_replace_zero(self):
        matrix = [[1, 2, 0, 7], [3, 1, 2, 0], [0, 3, 1, 2], [0, 0, 3, 1]]
        self.assertRaises(Exception, get_tridiagonal_determinant, matrix)

    def test_first_order(self):
        matrix = [[1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 1)

    def test_second_order(self):
        matrix = [[1, 2], [2, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -3)

    def test_third_order(self):
        matrix = [[1, -2, 0], [-4, 1, -2], [0, -4, 1]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -15)

    def test_fourth_order(self):
        matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 421)

    def test_zero_main_diagonal(self):
        matrix = [[0, 2], [3, 0]]
        self.assertEqual(get_tridiagonal_determinant(matrix), -6)

    def test_zero_sub_diagonal(self):
        matrix = [[3, 7, 0], [0, 3, 7], [0, 0, 3]]
        self.assertEqual(get_tridiagonal_determinant(matrix), 27)

    def test_fifth_order(self):
        matrix = [
            [2, 1, 0, 0, 0],
            [1, 2, 1, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 0, 1, 2, 1],
            [0, 0, 0, 1, 2],
        ]
        self.assertEqual(get_tridiagonal_determinant(matrix), 6)


if __name__ == "__main__":
    unittest.main()
