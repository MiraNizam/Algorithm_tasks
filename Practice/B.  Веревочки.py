"""
В. Веревочки

Есть n веревочек, нужно нарезать из них k кусков одинаковой длины. Найдите максимальную длину кусков, которые можно
получить.

Входные данные
В первой строке заданы два числа — n и k (1≤n,k≤10000). Далее в каждой из последующих n строк записано по одному числу
 — длине очередной веревочки ai (1≤ai≤107).

Выходные данные
Выведите одно вещественное число — максимальную длину кусков, которые можно получить. Ответ будет считаться верным,
если относительная или абсолютная погрешность не превышает 10−6.

Пример
входные данные
4
11
802
743
457
539
выходные данные
200.5
"""


def search_length(strings_array, k, mid):
    counter = 0
    for i in strings_array:
        counter += i // mid
    return counter >= k


def cut_strings():
    n, k = int(input()), int(input())
    strings_array = [int(input()) for _ in range(n)]

    l = 1
    r = max(strings_array)

    while r - l > 1e-8:
        mid = (r + l) / 2
        if search_length(strings_array, k, mid):
            l = mid
        else:
            r = mid
    return round(l, 1)


if __name__ == "__main__":
    print(cut_strings())