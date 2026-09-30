def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    validate(matrix)
    return calculate_determinant_recursive(matrix)


def validate(matrix):
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком.")

    if len(matrix) == 0:
        raise Exception("Матрица не должна быть пустой.")

    order = len(matrix)

    for row in matrix:
        if not isinstance(row, list):
            raise Exception("Строки матрицы должны быть списками.")

        if len(row) != order:
            raise Exception("Матрица должна быть квадратной.")

        if not all(is_integer(element) for element in row):
            raise Exception("Элементы матрицы должны быть целыми числами.")


def is_integer(element) -> bool:
    return isinstance(element, int) and not isinstance(element, bool)


def calculate_determinant_recursive(matrix: list[list[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]

    determinant = 0

    for column in range(len(matrix)):
        # Слагаемое с нулевым элементом равно нулю, минор для него не считаем
        if matrix[0][column] == 0:
            continue

        reduced_matrix = []

        for row in matrix[1:]:
            reduced_matrix.append(row[:column] + row[column + 1 :])

        minor = calculate_determinant_recursive(reduced_matrix)
        determinant += matrix[0][column] * (-1) ** column * minor

    return determinant


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
