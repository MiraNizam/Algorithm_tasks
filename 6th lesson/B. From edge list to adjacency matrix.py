"""
B. Перевести список ребер в матрицу смежности

Cписок рёбер ориентированного графа надо переводить в матрицу смежности.
Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 100) и число рёбер m (1 ≤ m ≤ n(n-1)). В следующих m строках заданы ребра
в виде пар вершин (u,v), если ребро ведет от u к v.

Формат вывода
Выведите матрицу смежности n на n. На пересечении i-й строки и j-го столбца стоит единица, если есть ребро, ведущее из
i в j.


"""

def adjacency_matrix(n, m, edge_list):
    adjacency_matrix = []

    for _ in range(n):
        adjacency_matrix.append([0] * n)

    for u, v in edge_list:
        adjacency_matrix[u-1][v-1] = 1

    for i in adjacency_matrix:
        print(" ".join(map(str, i)), sep="\n")


def main():
    n, m = tuple(map(int, (input().split(" ")))) # number vertex, number edge
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)]
    adjacency_matrix(n, m, edge_list)


if __name__ == "__main__":
    main()