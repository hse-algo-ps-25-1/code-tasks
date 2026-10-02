from functools import cache


def valid_matrix(matrix):
    if not isinstance(matrix, (list, tuple)) or len(matrix)==0:
        return False
    for row in matrix:
        if not isinstance(row, (list, tuple)) or len(row) != len(matrix):
            return False
        for val in row:
            if isinstance(val, bool) or not isinstance(val, (int, float)) or not val.is_integer():
                return False
    return True


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """

    @cache
    def determinant_recursive(matrix):
        matrix_order = len(matrix)

        if matrix_order == 1:
            return matrix[0][0]

        determinant = 0
        for col in range(matrix_order):
            if matrix[0][col]==0:
                continue
            submatrix = tuple(
                tuple(matrix[elem][row] for row in range(matrix_order) if row != col)
                for elem in range(1, matrix_order)
            )
            determinant += (
                ((-1) ** col) * matrix[0][col] * determinant_recursive(submatrix)
            )

        return determinant

    if not valid_matrix(matrix):
        raise Exception("Ошибка: неверный формат матрицы")
    # конвертация в кортежи для оптимизации расходов памяти и добавления возможности кэширования
    matrix = tuple(tuple(row) for row in matrix)
    return int(determinant_recursive(matrix))


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
