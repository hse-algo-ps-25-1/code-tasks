def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель разложением по строке.

    :param matrix: квадратная целочисленная матрица порядка не меньше 1
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    if not matrix or len(matrix) == 0:
        raise Exception("Матрица не должна быть пустой")
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком (list)")
    if any(not isinstance(row, list) for row in matrix):
        raise Exception("Каждая строка в матрице должна быть списком (list)")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise Exception("Матрица должна быть квадратной")
    if any(not isinstance(value, int) for row in matrix for value in row):
        raise Exception("Все элементы матрицы должны быть целыми числами (int)")

    if n == 1:
        return matrix[0][0]

    determinant = 0
    for j, element in enumerate(matrix[0]):
        minor = [row[:j] + row[j + 1 :] for row in matrix[1:]]
        determinant += (-1) ** j * element * calculate_determinant(minor)

    return determinant


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
