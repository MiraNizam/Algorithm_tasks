"""
Найдите такое число х, что х^2 + кв.корень от x = с

Вход:
вещественное число с

Вывод:
вывести х

Пример:

Вход:
2.0
Вывод:
1.0

"""
from math import sqrt


def f(mid, c):
    return mid*mid + sqrt(mid) == c


def main():
    c = float(input())
    l = 0
    r = c
    while r-l > 0.000001:
        mid = (r + l) / 2.0
        if f(mid, c):
            r = mid
        else:
            l = mid
    return r


if __name__ == "__main__":
    print(main())