"""
L. Два велосипеда

Ваша задача — по заданной стоимости велосипеда определить
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 10^6.
В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания.
В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 10^6.
Формат вывода
Нужно вывести два числа — номера дней по условию задачи.
Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.
"""

days = int(input())
money_by_days = list(map(int, input().split(" ")))
cycle_cost = int(input())
start = 0


def binary_search(left, right, money, cycle_cost):
    mid_day = (left + right) // 2

    if money[-1] < cycle_cost:
        return -1

    elif money[mid_day - 1] < cycle_cost <= money[mid_day] or mid_day == 0:
        return mid_day + 1

    elif money[mid_day] >= cycle_cost:
        return binary_search(left, mid_day, money, cycle_cost)

    else: #money[mid_day] < cycle_cost:
        return binary_search(mid_day, right, money, cycle_cost)


if __name__ == "__main__":
    one_cycle = binary_search(start, days, money_by_days, cycle_cost)
    two_cycle = binary_search(start, days, money_by_days, cycle_cost * 2)
    print(f"{one_cycle} {two_cycle}")





