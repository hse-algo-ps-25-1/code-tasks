def check_square_matrix(matrix: list[list[int]]) -> None:
    """Проверяет, что matrix является непустой квадратной матрицей
    из целых чисел.

    :param matrix: проверяемая матрица
    :raises Exception: если matrix не является такой матрицей
    """
    if not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком строк")

    n = len(matrix)
    if n == 0:
        raise Exception("Матрица не должна быть пустой")

    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            raise Exception("Матрица должна быть квадратной")
        for element in row:
            if type(element) is not int:
                raise Exception("Элементы матрицы должны быть целыми числами")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Итеративное вычисление определителя трёхдиагональной матрицы.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    check_square_matrix(matrix)
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    for row in range(n):
        if (
            matrix[row][row] != a
            or (row < n - 1 and matrix[row][row + 1] != b)
            or (row > 0 and matrix[row][row - 1] != c)
        ):
            raise Exception(
                "Матрица должна быть с постоянными значениями на диагоналях"
            )
        for col in range(n):
            if abs(row - col) > 1 and matrix[row][col] != 0:
                raise Exception("Остальные элементы матрицы должны быть равны нулю")

    # X_(n) = a * X_(n - 1) - b * c * X_(n - 2)
    prev2 = 1  # X_(0)
    prev1 = a  # X_(1)
    for _ in range(2, n + 1):
        current = a * prev1 - b * c * prev2
        prev2 = prev1
        prev1 = current

    return prev1


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
