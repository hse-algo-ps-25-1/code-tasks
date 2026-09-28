def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """

    validate(matrix)
    a, b, c = get_values(matrix)
    n = len(matrix)

    return __get_tridiagonal_determinant(a, b, c, n)


def get_values(matrix):
    a = matrix[0][0]
    b = 0
    c = 0
    if len(matrix) > 1:
        b = matrix[0][1]
        c = matrix[1][0]

    return (a, b, c)


def validate(matrix):
    if not isinstance(matrix, list):
        raise Exception("Неправильный тип матрицы!")

    n = len(matrix)
    if n < 1:
        raise Exception("Неправильный порядок матрицы!")

    for row in matrix:
        if len(row) != n:
            raise Exception("Матрица не квадратная!")

    a, b, c = get_values(matrix)

    if n > 1:
        # В трёхдиагональной матрице элементы в наддиагонали и поддиагонали
        # не равны нулю, иначе это не трёхдиагональная матрица
        if b == 0 or c == 0:
            raise Exception("Матрица не трёхдиагональная!")

    for i in range(n):
        for j in range(n):
            if not isinstance(matrix[i][j], int):
                raise Exception(
                    f"Есть нецелочисленный элемент матрицы в строке {i}, столбце {j}!"
                )

            # Проверка структуры вынесена в отдельную функцию
            # Поскольку было предупреждение ruff C901
            validate_matrix_structure(i, j, matrix, a, b, c)


def validate_matrix_structure(i, j, matrix, a, b, c):
    if i == j:
        if matrix[i][j] != a:
            raise Exception("Непостоянные значения на главной диагонали!")
    elif i == j - 1:
        if matrix[i][j] != b:
            raise Exception("Непостоянные значения на наддиагонали!")
    elif i == j + 1:
        if matrix[i][j] != c:
            raise Exception("Непостоянные значения на поддиагонали!")
    else:
        if matrix[i][j] != 0:
            raise Exception("Ненулевой элемент вне трёх диагоналей!")


def __get_tridiagonal_determinant(a, b, c, n):
    if n == 1:
        return a

    if n == 2:
        return a**2 - b * c

    return a * __get_tridiagonal_determinant(
        a, b, c, n - 1
    ) - b * c * __get_tridiagonal_determinant(a, b, c, n - 2)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
