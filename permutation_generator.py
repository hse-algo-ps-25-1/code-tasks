from collections.abc import Generator


def generate_permutations(elements: list) -> Generator[list, None, None]:
    """Выдаёт все перестановки элементов списка по одной.

    Каждая следующая получается из предыдущей. Рекурсия не используется.
    Порядок выдачи лексикографический. Повторы и пропуски недопустимы.

    :param elements: список любых сравнимых элементов
    :raises TypeError: аргумент не является списком
    :return: генератор перестановок; для пустого списка — одна пустая
        перестановка
    """
    if not isinstance(elements, list):
        raise TypeError("Аргумент должен быть списком")

    def _generator() -> Generator[list, None, None]:
        if not elements:
            yield []
            return

        current = sorted(elements)
        yield current.copy()

        n = len(current)
        while True:
            i = n - 2
            while i >= 0 and current[i] >= current[i + 1]:
                i -= 1

            if i < 0:
                break

            j = n - 1
            while current[j] <= current[i]:
                j -= 1

            current[i], current[j] = current[j], current[i]
            current[i + 1 :] = reversed(current[i + 1 :])

            yield current.copy()

    return _generator()
