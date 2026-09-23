from profilehooks import profile


@profile
def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n in (1, 2):  # Условие выхода из рекурсии. По условию, 1-е и 2-е число Фибоначчи равно 1
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


@profile
def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    fib = [0] * (n+1)
    fib[1] = 1                          # массив чисел начиная с 0, первое число по порядку - 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


@profile
def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    last_numer_1, last_number_2 = 1, 1
    current_number_value = 1
    if n in range(1, 2):
        return 1
    for i in range(3, n+1):
        last_number_2 = last_numer_1
        last_numer_1 = current_number_value
        current_number_value = last_numer_1 + last_number_2

    return current_number_value


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно: ")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно: ")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива: ")
    print(fibonacci(n))


if __name__ == "__main__":
    main()

