from typing import Any

NOT_LIST_ERROR_MSG = "Аргумент elements не является списком"


def _validate_elements(elements: Any) -> None:
    """Проверяет, что переданный аргумент является списком."""
    if type(elements) is not list:
        raise TypeError(NOT_LIST_ERROR_MSG)


def _permute_recursive(items: list[Any]) -> list[list[Any]]:
    """Внутренний рекурсивный генератор перестановок."""
    if len(items) <= 1:
        return [items[:]]

    result: list[list[Any]] = []
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i + 1 :]
        for p in _permute_recursive(remaining):
            result.append([current] + p)

    return result


def generate_permutations_rec(elements: list[Any]) -> list[list[Any]]:
    """Возвращает все перестановки элементов списка.

    Порядок перестановок в списке не фиксируется. Повторы и пропуски
    недопустимы.

    :param elements: список любых элементов
    :raises TypeError: аргумент не является списком
    :return: список перестановок; для пустого списка — список из одной
        пустой перестановки
    """
    _validate_elements(elements)
    return _permute_recursive(elements)


def generate_permutations_iter(elements: list[Any]) -> list[list[Any]]:
    """Возвращает все перестановки элементов списка.

    Итеративная реализация, без рекурсии. Порядок перестановок
    в списке не фиксируется. Повторы и пропуски недопустимы.

    :param elements: список любых элементов
    :raises TypeError: аргумент не является списком
    :return: список перестановок; для пустого списка — список из одной
        пустой перестановки
    """
    _validate_elements(elements)
    result: list[list[Any]] = [[]]

    for item in elements:
        next_permutations: list[list[Any]] = []
        for permutation in result:
            for i in range(len(permutation) + 1):
                next_permutations.append(permutation[:i] + [item] + permutation[i:])
        result = next_permutations

    return result

def main():
    for elements in ([], ["a"], ["a", "b", "c"]):
        print(f"{elements}, рекурсивно: {generate_permutations_rec(elements)}")
        print(f"{elements}, итеративно: {generate_permutations_iter(elements)}")


if __name__ == "__main__":
    main()
