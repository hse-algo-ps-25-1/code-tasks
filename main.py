def validate(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Матрица не должна быть пустым списком")

    size = len(matrix)

    for row in matrix:
        if not isinstance(row, list):
            raise Exception("Каждая строка матрицы должен быть списком")
        if len(row) != size:
            raise Exception("Матрица должна быть квадратной")
        for element in row:
            if not isinstance(element, int):
                raise Exception("Элементы матрицы должны быть целым числом")


def calculate_determinant(matrix: list[list[int]], validatation=True) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if validatation:
        validate(matrix)

    if len(matrix) == 1:
        return matrix[0][0]

    det = 0

    for column in range(len(matrix)):
        minor = []
        for row in matrix[1:]:
            minor.append(row[:column] + row[column + 1 :])

        det += matrix[0][column] * (-1) ** column * calculate_determinant(minor, False)
    return det


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
