"""
G. Гардероб

Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода
В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000. Во второй строке даётся
массив, в котором указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

Формат вывода
Нужно вывести в строку через пробел цвета предметов в правильном порядке.
"""


def counting_sort():
    n = int(input())
    data = input()
    if n == 0:
        return data

    array = list(map(int, data.split(" ")))
    counted_values = [0] * 3
    for value in array:
        counted_values[value] += 1

    result = []
    for value in range(3):
        result.extend(str(value) * counted_values[value])
    return " ".join(result)


if __name__ == "__main__":
    print(counting_sort())
