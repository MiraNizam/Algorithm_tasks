"""
Рюкзак с наибольшей стоимостью и восстановлением ответа
"""

def knapsack(n, max_weight, w, c):
    knapsack = []
    for i in range(n + 1):
        knapsack.append([])
        for j in range(max_weight + 1):
            knapsack[i].append([-1, -1])

    knapsack[0][0] = [0, 0]

    for i in range(1, n + 1):
        for j in range(max_weight + 1):
            knapsack[i][j] = knapsack[i -1][j][:]
        for now_weight in range(max_weight - w[i], -1, -1):
            if knapsack[i][now_weight][0] != -1 and knapsack[i][now_weight + w[i]][0] < knapsack[i][now_weight][0] + c[i]:
                knapsack[i][now_weight + w[i]][0] = knapsack[i][now_weight][0] + c[i] # запоминаем стоимость
                knapsack[i][now_weight + w[i]][1] = i # запоминаем номер предмета

    now_line = n
    max_cost_weight = 0
    for now_weight in range(max_weight + 1):
        if knapsack[now_line][now_weight][0] > knapsack[now_line][max_cost_weight][0]:
            max_cost_weight = now_weight

    now_item = knapsack[now_line][max_cost_weight][1]
    while now_item > 0:
        print(knapsack[now_item][max_cost_weight][1])
        max_cost_weight -= w[now_item]
        now_item = knapsack[now_item - 1][max_cost_weight][1]

if __name__ == "__main__":
    n, max_weight = map(int, input().split())
    w = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))