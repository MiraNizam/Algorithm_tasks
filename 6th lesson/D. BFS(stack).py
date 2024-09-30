"""
D. BFS

Задан неориентированный граф. Обойдите поиском в ширину все вершины, достижимые из заданной вершины s, и выведите их в
порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины
s (1 ≤ s ≤ n).

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться
в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).

"""

from collections import defaultdict, deque

def adjacency_list(edge_list):
    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list


def bfs(color, adjacency_dict, s):
    result = []
    planned = deque()
    planned.append(s)
    color[s] = "gray"
    while planned:
        u = planned.popleft()
        for neighbour in sorted(adjacency_dict[u]):
            if color[neighbour] == "white":
                color[neighbour] = "gray"
                planned.append(neighbour)
        color[u] = "black"
        result.append(u)
    return result


def main():
    n, m = tuple(map(int, (input().split(" ")))) # number vertex, number edge
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)]
    s = int(input())
    adjacency_dict = adjacency_list(edge_list)
    color = ["white"] * (n + 1)
    result = bfs(color, adjacency_dict, s)

    return " ".join(map(str, result))


if __name__ == "__main__":
    print(main())