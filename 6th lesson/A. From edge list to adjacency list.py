"""
 Написать программу, которая по списку рёбер графа будет строить его список смежности.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число ребер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра
в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите информацию о рёбрах, исходящих из каждой вершины.

В строке i надо написать число рёбер, исходящих из вершины i, а затем перечислить вершины, в которые ведут эти рёбра –—
в порядке возрастания их номеров.

"""
from collections import defaultdict


def adjacency_list(n, m, edge_list):
    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)

    for i in range(1, n + 1):
        print(len(adjacency_list[i]), " ".join(map(str, adjacency_list[i])), sep=" ")


def main():
    n, m = tuple(map(int, (input().split(" ")))) # number vertex, number edge
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)]
    adjacency_list(n, m, edge_list)


if __name__ == "__main__":
    main()