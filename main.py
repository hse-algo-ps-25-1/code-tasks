def _is_square_int_matrix(matrix: object) -> bool:
    """Проверяет, является ли объект непустой квадратной целичисленной матрицей.

    :param matrix: произвольный объект для валидации
    :return: True, если matrix - это непустой list[list[int]] размера N x N (без bool),
    иначе False
    """
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


def _calculate_determinant_rec(matrix: list[list[int]]) -> int:
    """Внутренняя рекурсивная функция вычисления определителя.

    Предполагает, что входная матрица уже прошла валидацию.

    :param matrix: квадратная целочисленная матрица
    :return: значение определителя
    """
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
        determinant += sign * value * _calculate_determinant_rec(minor)

    return determinant


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет опеределитель квадратной целочисленной матрицы разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raise ValueError: если matrix не является корректной квадратной матрицей
    :return: значение определителя
    """
    if not _is_square_int_matrix(matrix):
        raise ValueError("Ожидается непустая квадратная целочисленная матрица")

    return _calculate_determinant_rec(matrix)


def main() -> None:
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
