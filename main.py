def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трёхдиагональной матрицы."""
    _validate(matrix)

    size = len(matrix)
    a = matrix[0][0]

    if size == 1:
        return a

    b = matrix[0][1]
    c = matrix[1][0]

    determinant, _ = _get_two_determinants(size, a, b * c)
    return determinant


def _get_two_determinants(size: int, a: int, bc: int) -> tuple[int, int]:
    if size == 1:
        return a, 1

    previous, before_previous = _get_two_determinants(size - 1, a, bc)
    current = a * previous - bc * before_previous

    return current, previous


def _validate(matrix: list[list[int]]) -> None:
    if matrix is None:
        raise Exception("Объект не является матрицей!")

    n = len(matrix)
    if n == 0:
        raise Exception("Матрица пустая!")

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise Exception("Строка не является списком!")

        if len(row) != n:
            raise Exception("Матрица не квадратная!")

        for j, val in enumerate(row):
            if not isinstance(val, int) or isinstance(val, bool):
                raise Exception("Элементы матрицы имеют тип отличный от int!")

    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Матрица не является трёхдиагональной!")


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
