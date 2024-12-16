"""
На стол в ряд выложены карточки, на каждой карточке написано натуральное число. За один ход разрешается взять карточку
либо с левого, либо с правого конца ряда. Всего можно сделать k ходов. Итоговый счет равен сумме чисел на выбранных
карточках. Определите, какой максимальный счет можно получить по итогам игры. Вы можете воспользоваться заготовками
кода для данной задачи из репозитория курса

Формат ввода
В первой строке записано число карточек n (1≤n≤105).
Во второй строке записано число ходов k (1≤k≤n). В третьей строке через пробел даны числа, записанные на карточках.
i-е по счету число записано на i-й слева карточке. Все числа натуральные и не превосходят 104.

Формат вывода
Выведите единственное число —- максимальную сумму очков, которую можно набрать, сделав k ходов.

Пример 1
Ввод
7
3
5 8 2 1 3 4 11
Вывод
24

-- ПРИНЦИП РАБОТЫ и СЛОЖНОСТЬ --

Задачу можно решить через:

ДП - сложность O(k^2),
метод скользящего окна за О(k)


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мы используем метод скользящего окна для обновления текущей суммы. На каждой итерации мы вычитаем последнюю карту из
первой группы и добавляем карту из второй группы (с конца).

-- ID успешной посылки --
https://contest.yandex.ru/contest/34147/problems/?success=130106594#51450/2021_12_30/JQQNZeXB1n

"""


def get_card_count(n: int, k: int, cards: list) -> int:
    """через ДП"""
    if k >= n:
        return sum(cards)

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + cards[i - 1]

    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for j in range(i, 0, -1):
            if i == j:
                dp[j] = prefix_sum[j]
            else:
                dp[j] = dp[j] + cards[n - (i - j)]
    dp[0] = prefix_sum[n] - prefix_sum[n - k]
    return max(dp)

n = int(input())
k = int(input())
cards = list(map(int, input().split()))
print(get_card_count(n, k, cards))


def get_card_count(n: int, k: int, cards: list) -> int:
    """ через скользящее окно"""
    if k >= n:
        return sum(cards)

    current_sum = sum(cards[:k])
    max_sum = current_sum

    for i in range(1, k + 1):
        current_sum = current_sum - cards[k - i] + cards[n - i]
        max_sum = max(max_sum, current_sum)

    return max_sum

n = int(input())
k = int(input())
cards = list(map(int, input().split()))
print(get_card_count(n, k, cards))