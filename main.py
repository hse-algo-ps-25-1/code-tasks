LENGTH_NOT_INT = "Длина строки не является целым числом"
LENGTH_NOT_POS = "Длина строки меньше единицы"
NOT_LIST = "Набор строк не является списком"


def _validate_length(length: int) -> None:
    """Проверяет целочисленный тип длины и нижнюю границу 1."""
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError(LENGTH_NOT_INT)
    if length < 1:
        raise ValueError(LENGTH_NOT_POS)


def generate_strings_naive(length: int) -> list[str]:
    """Возвращает все строки длины length из 0 и 1 без двух нулей подряд.

    Набор строится наивно: перебираются все строки из 0 и 1 заданной длины,
    затем отбрасываются строки, в которых два нуля стоят рядом.
    Порядок строк не фиксируется.

    :param length: длина строки, целое число не меньше 1
    :raise TypeError: если length не целое
    :raise ValueError: если length меньше единицы
    :return: список строк
    """
    _validate_length(length)
    strings = []
    for number in range(2**length):
        string = f"{number:0{length}b}"
        if "00" not in string:
            strings.append(string)
    return strings


def check_zero_one_strings(length: int, strings: list[str]) -> bool:
    """Проверяет, что strings — полный набор строк длины length из 0 и 1,
    в которых никакие два нуля не стоят рядом.

    Порядок строк не фиксируется. Повторы не допускаются.

    :param length: длина каждой строки, целое число не меньше 1
    :param strings: проверяемый набор строк
    :raise TypeError: если length не целое или strings не список
    :raise ValueError: если length меньше единицы
    :return: True, если набор полон и корректен, иначе False
    """
    _validate_length(length)
    if not isinstance(strings, list):
        raise TypeError(NOT_LIST)

    # a(0) = 1, a(1) = 2; a(n) = a(n - 1) + a(n - 2).
    previous, expected = 1, 2
    if expected > len(strings):
        return False
    for _ in range(length - 1):
        previous, expected = expected, previous + expected
        if expected > len(strings):
            return False
    if len(strings) != expected:
        return False

    seen = set()
    for string in strings:
        if not isinstance(string, str) or len(string) != length:
            return False
        if any(symbol not in "01" for symbol in string) or "00" in string:
            return False
        if string in seen:
            return False
        seen.add(string)
    return True


def main():
    length = 3
    generated = generate_strings_naive(length)
    print("Наивная генерация строк из 0 и 1")
    print(f"Длина: {length}")
    print(f"Набор: {generated}")
    print(f"Результат проверки: {check_zero_one_strings(length, generated)}")


if __name__ == "__main__":
    main()
