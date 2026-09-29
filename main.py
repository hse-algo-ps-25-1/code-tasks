def _validate_matrix(matrix: list[list[int]]) -> None:
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if not matrix:
        raise ValueError("matrix must not be empty")

    order = len(matrix)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix rows must be lists")
        if len(row) != order:
            raise ValueError("matrix must be square")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix elements must be integers")


def _validate_three_bands(matrix: list[list[int]]) -> int:
    order = len(matrix)
    diagonal = matrix[0][0]
    for index in range(order):
        if matrix[index][index] != diagonal:
            raise ValueError("main diagonal values must be equal")
        for column in range(order):
            if abs(index - column) > 1 and matrix[index][column] != 0:
                raise ValueError("elements outside the three diagonals must be zero")
    return diagonal


def _get_constant_off_diagonals(matrix: list[list[int]]) -> tuple[int, int]:
    order = len(matrix)
    upper = matrix[0][1]
    lower = matrix[1][0]
    for index in range(1, order - 1):
        if matrix[index][index + 1] != upper:
            raise ValueError("upper diagonal values must be equal")
        if matrix[index + 1][index] != lower:
            raise ValueError("lower diagonal values must be equal")
    return upper, lower


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Итеративное вычисление определителя трёхдиагональной матрицы.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises TypeError: если matrix или его элементы имеют неподходящий тип
    :raises ValueError: если matrix пуста, не квадратна или не соответствует
        условию о постоянных диагоналях
    :return: значение определителя
    """
    _validate_matrix(matrix)
    order = len(matrix)
    diagonal = _validate_three_bands(matrix)
    if order == 1:
        return diagonal

    upper, lower = _get_constant_off_diagonals(matrix)

    # D_0 = 1, D_1 = a, D_k = a*D_(k-1) - b*c*D_(k-2).
    previous_previous = 1
    previous = diagonal
    for _ in range(2, order + 1):
        current = diagonal * previous - upper * lower * previous_previous
        previous_previous, previous = previous, current

    return previous


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
