from itertools import product

LENGTH_NOT_INT = "Длина строки не является целым числом"
LENGTH_NOT_POS = "Длина строки меньше единицы"
NOT_LIST = "Набор строк не является списком"


def _validate_length(length: int) -> None:
   
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError(LENGTH_NOT_INT)
    if length < 1:
        raise ValueError(LENGTH_NOT_POS)


def generate_strings_naive(length: int) -> list[str]:

    _validate_length(length)

    result = []
    for chars in product("01", repeat=length):
        string = "".join(chars)
        if "00" not in string:
            result.append(string)
    return result


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(LENGTH_NOT_POS)

    previous, current = 1, 2
    for _ in range(n):
        previous, current = current, previous + current
    return previous


def check_zero_one_strings(length: int, strings: list[str]) -> bool:
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError(LENGTH_NOT_INT)
    if not isinstance(strings, list):
        raise TypeError(NOT_LIST)
    if length < 1:
        raise ValueError(LENGTH_NOT_POS)

    count = fibonacci(length)
    if len(strings) != count:
        return False

    for string in strings:
        if not isinstance(string, str):
            return False
        if len(string) != length:
            return False
        if any(char not in "01" for char in string):
            return False
        if "00" in string:
            return False

    return len(set(strings)) == count


def main() -> None:
    length = 3
    generated = generate_strings_naive(length)
    print("Наивная генерация строк из 0 и 1")
    print(f"Длина: {length}")
    print(f"Набор: {generated}")
    print(f"Результат проверки: {check_zero_one_strings(length, generated)}")


if __name__ == "__main__":
    main()