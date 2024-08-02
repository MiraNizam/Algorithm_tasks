"""
A. Ближайший ноль

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n
одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать
расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в
том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 10^6). В следующей строке записаны n целых неотрицательных чисел —
номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один
ноль. Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.


https://contest.yandex.ru/contest/22450/run-report/116154179/
"""


def find_destination_to_null():
    street_length = int(input())
    home_numbers = list(map(int, input().split(" ")))

    left_null = home_numbers.index(0)
    right_null = street_length - 1 - home_numbers[::-1].index(0)

    left_checking = []
    right_checking = []

    count = 0
    for i in range(street_length):
        if home_numbers[i] == 0:
            left_checking.append(0)
            count = 0
        elif home_numbers[i] != 0 and left_null > i:
            left_checking.append(street_length)
        else:
            count += 1
            left_checking.append(count)

    count = 0
    for i in range(street_length)[::-1]:
        if home_numbers[i] == 0:
            right_checking.append(0)
            count = 0
        elif home_numbers[i] != 0 and right_null < i:
            right_checking.append(street_length)
        else:
            count += 1
            right_checking.append(count)

    right_checking.reverse()

    result = []
    for i in range(street_length):
        destination_to_null = min(left_checking[i], right_checking[i])
        result.append(destination_to_null)

    return " ".join([str(i) for i in result])


if __name__ == "__main__":
    print(find_destination_to_null())
