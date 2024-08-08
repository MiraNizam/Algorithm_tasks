"""
H. Большое число
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

"""
from functools import cmp_to_key


massive_len = int(input())
massive = list(input().split(" "))


def comparator(lhs, rhs):
    if lhs + rhs > rhs + lhs:
        return -1
    else:
        return 1


def biggest_no(massive):
    sorted_massive = sorted(massive, key=cmp_to_key(comparator)) # необходимо написать компаратор, так как нам
    # нужно сравнить суммы двух элементов, а ключ принимает только один. к одному элементу мы приводим
    # с помощью метода cmp_to_key
    big_no = "".join(sorted_massive)
    return big_no


if __name__=="__main__":
    print(biggest_no(massive))
