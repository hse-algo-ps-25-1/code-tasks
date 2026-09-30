import random
from collections import namedtuple

Case = namedtuple("Case", ["matrix", "det"])

DIAGONAL_VALUES = (-3, -2, -1, 1, 2, 3)
ABOVE_DIAGONAL_VALUES = range(-5, 6)


def generate_matrix_and_det(order: int) -> Case:
    """Строит квадратную целочисленную матрицу заданного порядка
    с заранее известным определителем.

    Определитель получают из свойств, не вычисляя его разложением
    и не вызывая calculate_determinant.

    :param order: порядок матрицы, целое число не меньше 1
    :raises Exception: если order не является таким числом
    :return: Case с полями matrix и det
    """
    validate_order(order)
    matrix, determinant = build_triangular_matrix(order)
    add_upper_rows(matrix)
    add_right_columns(matrix)
    swap_count = swap_random_pairs(matrix)
    if swap_count % 2 == 1:
        determinant = -determinant
    return Case(matrix, determinant)


def validate_order(order: int) -> None:
    if not isinstance(order, int) or isinstance(order, bool):
        raise Exception("Порядок матрицы должен быть целым числом.")

    if order < 1:
        raise Exception("Порядок матрицы должен быть не меньше 1.")


def random_sign() -> int:
    return random.choice((1, -1))


def build_triangular_matrix(order: int) -> tuple[list[list[int]], int]:
    matrix = []
    determinant = 1
    for row_index in range(order):
        row = [0] * order
        row[row_index] = random.choice(DIAGONAL_VALUES)
        for column_index in range(row_index + 1, order):
            row[column_index] = random.choice(ABOVE_DIAGONAL_VALUES)
        determinant *= row[row_index]
        matrix.append(row)
    return matrix, determinant


def add_upper_rows(matrix: list[list[int]]) -> None:
    order = len(matrix)
    for target in range(order - 1, 0, -1):
        for source in range(target):
            add_row(matrix, target, source, random_sign())


def add_right_columns(matrix: list[list[int]]) -> None:
    order = len(matrix)
    for target in range(order - 1):
        for source in range(target + 1, order):
            add_column(matrix, target, source, random_sign())


def add_row(matrix: list[list[int]], target: int, source: int, factor: int) -> None:
    for column, source_value in enumerate(matrix[source]):
        matrix[target][column] += factor * source_value


def add_column(matrix: list[list[int]], target: int, source: int, factor: int) -> None:
    for row in matrix:
        row[target] += factor * row[source]


def swap_random_pairs(matrix: list[list[int]]) -> int:
    order = len(matrix)
    if order == 1:
        return 0

    row_swap_count = random_swap_count(order)
    for _ in range(row_swap_count):
        first, second = random.sample(range(order), 2)
        swap_rows(matrix, first, second)

    column_swap_count = random_swap_count(order)
    for _ in range(column_swap_count):
        first, second = random.sample(range(order), 2)
        swap_columns(matrix, first, second)

    return row_swap_count + column_swap_count


def random_swap_count(order: int) -> int:
    return order + random.randint(0, order)


def swap_rows(matrix: list[list[int]], first: int, second: int) -> None:
    matrix[first], matrix[second] = matrix[second], matrix[first]


def swap_columns(matrix: list[list[int]], first: int, second: int) -> None:
    for row in matrix:
        row[first], row[second] = row[second], row[first]


def main():
    n = 10
    print(f"Генерация матрицы порядка {n}")
    result = generate_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result.det)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result.matrix]))


if __name__ == "__main__":
    main()
