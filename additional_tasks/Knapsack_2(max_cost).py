def knapsack(n, max_weight, w, c):
    knapsack = [-1] * (max_weight + 1)
    knapsack[0] = 0 # храним не просто признак, что можем собрать вес, а с какой max стоимостью

    for i in range(n): # по очереди берем предметы
        for now_weight in range(max_weight - w[i], -1, -1):
            if knapsack[now_weight] != -1: # если вес -1, значит пока этот вес набрать не можем, иначе ниже
                knapsack[now_weight + w[i]] = max(knapsack[now_weight + w[i]], knapsack[now_weight] + c[i])

    ans = 0
    for now_weight in range(max_weight, -1, -1):
        ans = max(ans, knapsack[now_weight])
    print(ans)


if __name__ == "__main__":
    n, max_weight = map(int, input().split())
    w = list(map(int, input().split()))
    c = list(map(int, input().split()))
