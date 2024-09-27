"""
C. DFS

Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые из заданной вершины s, и выведите их в
порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины s
(1 ≤ s ≤ n). В графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""

from collections import defaultdict


def adjacency_list(edge_list):
    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list


def dfs(adjacency_dict, s, color, result):
    stack = []
    stack.append(s)  # Добавляем стартовую вершину в стек.

    while stack: # Пока стек не пуст:
        # Получаем из стека очередную вершину.
        # Это может быть как новая вершина, так и уже посещённая однажды.
        v = stack.pop()

        if color[v - 1] == 'white':
            # Красим вершину в серый. И сразу кладём её обратно в стек:
            # это позволит алгоритму позднее вспомнить обратный путь по графу.
            color[v - 1] = 'gray'
            result.append(v)
            stack.append(v)

            # Теперь добавляем в стек все непосещённые соседние вершины, вместо вызова рекурсии
            for w in sorted(adjacency_dict[v], reverse=True):
                # Для каждого исходящего ребра (v, w):
                if color[w - 1] == 'white':
                    stack.append(w)

        elif color[v - 1] == 'gray':
        # Серую вершину мы могли получить из стека только на обратном пути.
        # Следовательно, её следует перекрасить в чёрный.
            color[v - 1] = 'black'

def main():
    n, m = tuple(map(int, (input().split(" ")))) # number vertex, number edge
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)]
    s = int(input())
    adjacency_dict = adjacency_list(edge_list)
    color = ["white"] * (n + 1)
    result = []

    dfs(adjacency_dict, s, color, result) # start vertex

    return " ".join(map(str, result))


if __name__ == "__main__":
    print(main())
