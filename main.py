from functools import cache


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """

    def valid_matrix(matrix):
        if not matrix or type(matrix) is not list:
            return False
        for row in matrix:
            if type(row) is not list or len(row) != len(matrix):
                return False
            for val in row:
                if not val.is_integer():
                    return False
        return True

    @cache
    def determinant_recursive(matrix):
        matrix_order = len(matrix)

        if matrix_order == 1:
            return matrix[0][0]
        if matrix_order == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for col_idx in range(matrix_order):
            minor = tuple(
                tuple(matrix[elem][row] for row in range(matrix_order) if row != col_idx)
                for elem in range(1, matrix_order)
            )

            sign = 1 if col_idx % 2 == 0 else -1
            determinant += sign * matrix[0][col_idx] * determinant_recursive(minor)

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
