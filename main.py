def _is_square_int_matrix(matrix: object) -> bool:
    if not isinstance(matrix, list) or not matrix:
        return False
    order = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != order:
            return False
        for value in row:
            if not isinstance(value, int) or isinstance(value, bool):
                return False
    return True


def calculate_determinant(matrix: list[list[int]], validated: bool = True) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :param validate: проверять вход (True - только на верхнем вызове)
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if validated and not _is_square_int_matrix(matrix):
        raise ValueError("Ожидается непустая квадратная целочисленная матрица")

    order = len(matrix)
    if order == 1:
        return matrix[0][0]

    determinant = 0
    for column, value in enumerate(matrix[0]):
        minor = []
        for row in matrix[1:]:
            row_copy = row[:]
            del row_copy[column]
            minor.append(row_copy)
        sign = 1 if column % 2 == 0 else -1
        determinant += sign * value * calculate_determinant(minor, validated=False)

    return determinant


def main() -> None:
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
