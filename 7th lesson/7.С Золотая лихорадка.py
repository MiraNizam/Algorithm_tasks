"""
C. Золотая лихорадка

Есть с собой рюкзак грузоподъёмностью до M килограмм.

Всего золотых куч n штук, и все они разные. В куче под номером i содержится mi килограммов золотого песка, а стоимость
одного килограмма — ci алгосских франков.

Необходимо наполнить рюкзак так, чтобы общая стоимость золотого песка в пересчёте на франки была максимальной.

Формат ввода
В первой строке задано целое число M — грузоподъёмность рюкзака Гоши (0 ≤ M ≤ 108).

Во второй строке дано количество куч с золотым песком — целое число n (1 ≤ n ≤ 105).

В каждой из следующих n строк описаны кучи: i-ая куча задаётся двумя целыми числами ci и mi, записанными через пробел
(1 ≤ ci ≤ 107, 1 ≤ mi ≤ 108).

Формат вывода
Выведите единственное число —– максимальную сумму (в алгосских франках), которую Гоша сможет вынести из пещеры в
своём рюкзаке.
"""


def max_backpack_capacity(m, n, heaps):
    loading = 0
    money = 0
    count = 0
    sorted_heaps = sorted(heaps, key=lambda x: (x[0], x[1]), reverse=True)
    while loading < m and count < n:
        for i in sorted_heaps:
            count += 1
            if i[1] <= m - loading:
                money += i[0] * i[1]
                loading += i[1]
            else:
                money += i[0] * (m - loading)
                loading += (m - loading)
    return money


def main():
    m = int(input())
    n = int(input())
    heaps = [(tuple(map(int, (input().split())))) for _ in range(n)]
    print(max_backpack_capacity(m, n, heaps))


if __name__ == "__main__":
    main()
