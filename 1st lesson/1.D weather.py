"""
D. Хаотичность погоды

Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше, чем в день до
(если такой существует) и в день после текущего (если такой существует). Например, если за 5 дней максимальная
температура воздуха составляла [1, 2, 5, 4, 8] градусов, то хаотичность за этот период равна 2: в 3-й и 5-й дни
выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.

Формат ввода
В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105. Во второй строке даны n целых чисел
–— значения температуры в каждый из n дней. Значения температуры не превосходят 273 по модулю.

Формат вывода
Выведите единственное число — хаотичность за данный период.

"""


def chaotic_weather():
    days = int(input())
    temperature = list(map(int, input().split(" ")))
    chaotic_index = 0
    if days == 1:
        chaotic_index += 1
        return chaotic_index
    for i in range(days):
        if i == 0:
            if temperature[i] > temperature[i+1]:
                chaotic_index += 1
        elif i == days - 1:
            if temperature[i] > temperature[i -1]:
                chaotic_index += 1
        elif temperature[i+1] < temperature[i] and temperature[i-1] < temperature[i]:
            chaotic_index += 1
    return chaotic_index


if __name__ == "__main__":
    print(chaotic_weather())