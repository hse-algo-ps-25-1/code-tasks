def _is_square_int_matrix(matrix: object) -> bool:
    if not isinstance(matrix, list) or not matrix:
        return False  # Не список или пустой
    order = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != order:
            return False  # строка не список или длина не совпадает
        for value in row:
            if not isinstance(value, int) or isinstance(value, bool):
                return False  # элемент не целый (bool целым не считаем)
    return True


def calculate_determinant(matrix: list[list[int]], validated: bool = True) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :param validate: проверять вход (True - только на верхнем вызове)
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if validated and not _is_square_int_matrix(
        matrix
    ):  # Проверка получается только на верхнем вызове
        raise ValueError("Ожидается непустая квадратная целочисленная матрица")

    order = len(matrix)
    if order == 1:
        return matrix[0][0]  # база

    determinant = 0
    for column, value in enumerate(matrix[0]):
        minor = []
        for row in matrix[1:]:
            row_copy = row[:]  # не трогаем исходную матрицу
            del row_copy[column]  # убираем столбец
            minor.append(row_copy)
        sign = 1 if column % 2 == 0 else -1  # знак (-1)^column
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
