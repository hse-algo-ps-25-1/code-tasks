from queue import Queue


def validate_args(month, lifetime):
    for arg in (month, lifetime):
        if isinstance(arg, bool) or not isinstance(arg, int):
            raise TypeError("аргументы должны быть целыми числами")
    if month < 1:
        raise ValueError("month должен быть не меньше 1")
    if lifetime < 2:
        raise ValueError("lifetime должен быть не меньше 2")


def rabbits(month: int, lifetime: int) -> int:
    """Возвращает количество живых пар кроликов в месяце month.

    В месяце 1 жива одна пара, родившаяся в этом месяце. Пара, родившаяся
    в месяце t, не приносит потомства в месяцах t и t + 1. С месяца t + 2
    она каждый месяц приносит одну новую пару, в том числе в месяц смерти.
    Пара живёт lifetime месяцев и входит в численность месяцев
    t, ..., t + lifetime - 1. В месяце t + lifetime она умирает и в число
    живых пар этого месяца не входит.

    :param month: номер месяца, целое число не меньше 1
    :param lifetime: продолжительность жизни в месяцах, целое число не меньше 2
    :raises TypeError: аргумент не целое число; bool не допускается
    :raises ValueError: month < 1 или lifetime < 2
    :return: число живых пар
    """
    validate_args(month, lifetime)

    born = Queue()
    born.enqueue(1)
    alive = 1
    last_born = 1
    for _ in range(2, month + 1):
        newborn = alive - last_born
        born.enqueue(newborn)
        alive += newborn
        if len(born) > lifetime:
            alive -= born.dequeue()
        last_born = newborn
    return alive


def main():
    queue = Queue()
    for value in (1, 2, 2):
        queue.enqueue(value)
    print("Начало очереди:", queue.peek())
    print("Вышло:", queue.dequeue())
    print("Пар на 8-й месяц при жизни 7 месяцев:", rabbits(8, 7))


if __name__ == "__main__":
    main()
