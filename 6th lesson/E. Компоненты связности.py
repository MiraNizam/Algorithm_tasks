"""
E. Компоненты связности

Вам дан неориентированный граф. Найдите его компоненты связности.

Формат ввода
В первой строке дано количество вершин n (1≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 2 ⋅ 105). В каждой из следующих m строк
записано по ребру в виде пары вершин 1 ≤ u, v ≤ n.

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите все компоненты связности в следующем формате: в первой строке выведите общее количество компонент.

Затем на отдельных строках выведите вершины каждой компоненты, отсортированные по возрастанию номеров. Компоненты
между собой упорядочивайте по номеру первой вершины.

"""

from collections import defaultdict


def adjacency_list(n, edge_list):
    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    for i in range(1, n + 1):
        if i not in adjacency_list:
            adjacency_list[i] = []
    return adjacency_list


def dfs(adjacency_dict, vertex, component_count, components):
    stack = [vertex]
    component_vertices = []

    while stack:
        v = stack.pop()

        if components[v] == -1:
            components[v] = component_count
            component_vertices.append(v)

            for w in sorted(adjacency_dict[v], reverse=True):
                if components[w] == -1:
                    stack.append(w)

    return sorted(component_vertices)


def main():
    n, m = map(int, input().split()) # number vertex, number edge
    edge_list = [list(map(int, (input().split()))) for _ in range(m)]
    adjacency_dict = adjacency_list(n, edge_list)
    components = [-1] * (n + 1)
    component_count = 1
    results = []

    for i in range(1, n+1):
        if components[i] == -1:
            results.append(dfs(adjacency_dict, i, component_count, components))
            component_count += 1

    print(len(results))
    for component in results:
        print(" ".join(map(str, component)))


if __name__ == "__main__":
    main()