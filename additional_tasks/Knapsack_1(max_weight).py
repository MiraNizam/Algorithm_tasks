def knapsack(n, max_weight, w): # пример: кол-во предметов = 3,макс_вес = 10, список предметов = [ 3, 5, 7]
    knapsack = [0] * (max_weight + 1)   # список по макс_весу с 0. knapsack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    knapsack[0] = 1 # knapsack = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(n): # по очереди берем предметы
        for now_weight in range(max_weight - w[i], -1, -1):  # max_weight - w[i] = 10 - 3 = 7 идем от 7 до 0
            if knapsack[now_weight] == 1:# knapsack[7] != 1 =>  без изменений, когда knapsack[0] == 1, то
                knapsack[now_weight + w[i]] = 1 # knapsack[0 + 3] = 1 knapsack = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    for now_weight in range(max_weight, -1, -1):# ищем максимальный вес now_weight от 10 до 0, для которого knapsack[now_weight] == 1
        if knapsack[now_weight] == 1: #
            print(now_weight) #
            break

if __name__ == "__main__":
    n, max_weight = map(int, input().split())
    w = list(map(int, input().split()))

