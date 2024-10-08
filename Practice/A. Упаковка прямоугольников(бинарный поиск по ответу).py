"""
A. Упаковка прямоугольников

Есть n прямоугольников одинакового размера: w в ширину и h в длину. Требуется найти квадрат минимального размера,
 в который можно упаковать данные прямоугольники. Прямоугольники при этом нельзя поворачивать.

Входные данные
Ввод содержит три целых числа: w, h, n (1≤w,h,n≤10^9).

Выходные данные
Выведите минимальную длину стороны квадрата, в который можно упаковать заданные прямоугольники.

Пример
входные данные
2 3 10
выходные данные
9

"""


def check_mid(w, h, n, mid):
    counter = (mid//w) * (mid//h)
    # counter - сколько прямоугольников влезает
    return counter >= n


def calculate_square():
    w = int(input())
    h = int(input())
    n = int(input())

    l = min(h, w) - 1
    r = max(h, w) * n + 1

    while r - l > 1:
        mid = (l + r) // 2
        # true - если в квадрат со стороной mid можно вписать n прямоугольников w на h
        if check_mid(w, h, n, mid):
            r = mid
        else:
            l = mid
    return r


if __name__ == "__main__":
    print(calculate_square())