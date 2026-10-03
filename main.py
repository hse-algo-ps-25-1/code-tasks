def stars_and_bars(n: int, k: int) -> list[str]:
    """Возвращает все представления распределений k одинаковых предметов
    по n различимым ящикам в формате «звёзды и перегородки».
    Реализована рекурсивно.

    Каждая строка состоит из k символов '*' и n-1 символа '|', без пробелов.
    Пустые ящики допускаются. Порядок строк в списке не регламентируется.

    :param n: число ящиков, целое не меньше 1
    :param k: число предметов, целое неотрицательное
    :raises Exception: если n или k не являются такими числами
    :return: список строк
    """

    validate(n, k)

    result = []
    distribution = [0] * n
    generate_stars_and_bars(distribution, result, n, current_box=0, remaining=k)

    return result


def generate_stars_and_bars(distribution, result, n, current_box, remaining):
    if current_box == n - 1:
        distribution[current_box] = remaining
        parts = []
        for count in distribution:
            parts.append("*" * count)
        result.append("|".join(parts))

        return

    for count in range(remaining + 1):
        distribution[current_box] = count
        generate_stars_and_bars(
            distribution, result, n, current_box + 1, remaining - count
        )


def validate(n, k):
    if not isinstance(n, int) or isinstance(n, bool):
        raise Exception("n должно быть целочисленным!")

    if not isinstance(k, int) or isinstance(k, bool):
        raise Exception("k должно быть целочисленным!")

    if n < 1:
        raise Exception("n должно быть больше или равно 1!")

    if k < 0:
        raise Exception("k не может быть отрицательным!")


def main():
    n = 3
    k = 3
    print(f"Распределения {k} предметов по {n} ящикам:")
    for item in stars_and_bars(n, k):
        print(item)


if __name__ == "__main__":
    main()
