def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Рекурсивное вычисление определителя трёхдиагональной матрицы разложением.

    :param matrix: квадратная целочисленная трёхдиагональная матрица
        порядка не меньше 1 с постоянными значениями на каждой
        из трёх диагоналей
    :raises Exception: если матрица, строки или элементы имеют неверный тип,
    либо если размер или структура не соответствуют требованиям
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
    """Проверяет типы, размер и структуру матрицы."""
    if not isinstance(matrix, list):
        raise Exception("Неправильный тип матрицы!")

    n = len(matrix)
    if n < 1:
        raise Exception("Неправильный порядок матрицы!")

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise Exception(f"Строка {i} не является списком!")

    for row in matrix:
        if len(row) != n:
            raise Exception("Матрица не квадратная!")

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if isinstance(value, bool) or not isinstance(value, int):
                raise Exception(
                    f"Элемент в строке {i}, столбце {j} должен быть целым числом!"
                )

    a, b, c = get_values(matrix)

    # Проверка структуры вынесена в отдельную функцию
    # Поскольку было предупреждение ruff C901
    validate_matrix_structure(matrix, a, b, c)


def validate_matrix_structure(matrix, a, b, c):
    """Проверяет постоянство 3 главных диагоналей и нули вне этих трёх диагоналей."""
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if i == j:
                if value != a:
                    raise Exception("Непостоянные значения на главной диагонали!")
            elif j == i + 1:
                if value != b:
                    raise Exception("Непостоянные значения на наддиагонали!")
            elif i == j + 1:
                if value != c:
                    raise Exception("Непостоянные значения на поддиагонали!")
            elif value != 0:
                raise Exception("Ненулевой элемент вне трёх диагоналей!")


def __get_tridiagonal_determinant(a, b, c, n):
    """Рекурсивное вычисление определителя с использованием рекуррентного соотношения и
    сохранением промежуточных результатов в словарь."""
    determinants = {
        1: a,
        2: a**2 - b * c,
    }

    def calculate(order: int) -> int:
        if order not in determinants:
            determinants[order] = a * calculate(order - 1) - b * c * calculate(
                order - 2
            )
        return determinants[order]

    return calculate(n)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
