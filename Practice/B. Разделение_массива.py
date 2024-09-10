"""
В. Разделение массива
Дан массив из n положительных целых чисел. Нужно разбить его на k отрезков так, чтобы максимальная сумма на отрезке была минимально возможной.

Выходные данные
Выведите одно число — минимально возможную максимальную сумму на отрезке.

Тест:
Ввод:
10
[1, 3, 2, 4, 10, 8, 4, 2, 5, 3]

Вывод: 12

Средняя временная сложность О(Nlog(SUM))
"""


def check_split(array, k, mid):
    counter = 1 # количество кусков
    current_sum = 0 # текущая сумма по массиву
    for num in array:
        current_sum += num
        if current_sum > mid:
            counter += 1
            current_sum = num
    return counter <= k


def split_array(): # бинарный поиск по ответу
    count = int(input())
    array = list(map(int, input().split(" ")))
    k = int(input()) # количество кусков
    l = max(array) - 1  # нижняя граница для бин поиска
    r = sum(array) + 1 # верхняя граница для бин поиска

    while r - l > 1:
        mid = (l + r) // 2
        print(mid)
        # true -> можно разбить массив на k кусков так что сумма любого куска  <= mid
        # false -> нельзя разбить массив на k кусков так что сумма любого куска  <= mid
        if check_split(array, k, mid):
            r = mid
        else:
            l = mid
    return r







if __name__ == "__main__":
    print(split_array())