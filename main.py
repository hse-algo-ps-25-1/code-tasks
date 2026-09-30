def __validate(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        raise ValueError("Матрица не должна быть пустой.")
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("Матрица должна быть квадратной.")

def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Итеративное вычисление определителя трёхдиагональной матрицы.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если matrix не является такой матрицей
    :return: значение определителя
    """
    __validate(matrix)
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]

    d1 = a
    d2 = a**2 - b * c

    if n == 2:
        return d2

    prev2 = d1
    prev1 = d2

    for k in range(3, n + 1):
        current = a * prev1 - b * c * prev2
        prev2 = prev1
        prev1 = current

    return prev1


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трёхдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
