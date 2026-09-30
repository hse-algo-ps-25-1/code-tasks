def _is_int(row):
    """Проверяет что все элементы строки - это целые числа
    :param row: строка матрицы
    :raises TypeError: при не совпадении типа
    :return: None
    """
    for x in row:
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError("matrix element is not int")


def _validate(matrix):
    """Проверяет что matrix квадратная целочисленная трёхдиагональная матрица
    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: None
    """
    if matrix is None:
        raise Exception("matrix is None")

    if not isinstance(matrix, list):
        raise Exception("matrix is not list")

    n = len(matrix)

    if n == 0:
        raise Exception("Matrix is empty")

    for row in matrix:
        if not isinstance(row, list):
            raise Exception("matrix is not list")

        if len(row) != n:
            raise Exception("matrix is not square")

        _is_int(row)

    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("matrix is not tridiagonal")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    _validate(matrix)

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]

    d1 = a
    d2 = a * a - b * c

    if n == 2:
        return d2

    def go(steps, prev2, prev1):
        if steps == 0:
            return prev1

        next_step = a * prev1 - b * c * prev2
        return go(steps - 1, prev1, next_step)

    return go(n - 2, d1, d2)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
