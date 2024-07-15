"""
H. Двоичная система

Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе. В
строенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.

"""

def binary_sum():
    a = str(input())
    b = str(input())

    a = a[::-1]
    b = b[::-1]

    max_length = max(len(a), len(b))

    a += "0" * (max_length - len(a))
    b += "0" * (max_length - len(b))

    reversed_sum = []
    next_place = 0
    for i in zip(a, b):
        place = int(i[0]) + int(i[1]) + next_place

        if place == 2:
            next_place = 1
            place = 0
            reversed_sum.append(place)
        elif place == 3:
            next_place = 1
            place = 1
            reversed_sum.append(place)
        elif place == 1:
            next_place = 0
            reversed_sum.append(place)
        else:
            reversed_sum.append(place)

    if next_place == 1:
        reversed_sum.append(next_place)

    sum = "".join([str(i) for i in reversed_sum])
    print(sum[::-1])


if __name__ == '__main__':
    binary_sum()
