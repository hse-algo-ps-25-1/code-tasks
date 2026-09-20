from functools import lru_cache


#Правильная работа кода гарантируется, если число n является целым и положительным.
#Также n-ое число фибоначчи не должно выходить за рамки максимального int в текущей среде выполнения

@lru_cache
def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: Порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n > 1:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    else:
        return n


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: Порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n < 2:
        return n
    fibonacci_numbers = [0, 1]
    for _ in range(2, n + 1):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[-1]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: Порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n < 2:
        return n

    f_num1, f_num2 = 0, 1
    for _ in range(2, n + 1):
        f_num1, f_num2 = f_num2, f_num1 + f_num2
    return f_num2


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
