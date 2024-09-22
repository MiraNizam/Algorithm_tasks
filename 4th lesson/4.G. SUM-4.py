"""
G. Сумма четвёрок

Формат ввода
В первой строке дано общее количество элементов массива n (0 ≤ n ≤ 1000).
Во второй строке дано целое число S.
В третьей строке задан сам массив. Каждое число является целым и не превосходит по модулю 1010.

Формат вывода
В первой строке выведите количество найденных четвёрок чисел.
В последующих строках выведите найденные четвёрки.
Числа внутри одной четверки должны быть упорядочены по возрастанию. Между собой четвёрки упорядочены лексикографически.
"""


def sum_four():
    n = int(input())
    if n == 0:
        print(0)
        return 0

    A = int(input())
    x = sorted(map(int, input().split(" ")))

    history = set()
    quatros = set()
    for i in range(n-3):
        for k in range(i + 1, n-2):
            for j in range(k + 1, n-1):
                target = A - x[i] - x[k] - x[j]
                if target in history:
                    quatros.add((target, x[i], x[k], x[j]))
        history.add(x[i])

    print(len(quatros))
    print("\n".join(" ".join(map(str, i)) for i in sorted(quatros)))
    return len(quatros), quatros


if __name__ == "__main__":
    sum_four()

