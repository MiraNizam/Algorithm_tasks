"""
J. Топологическая сортировка

Дан ациклический ориентированный граф (так называемый DAG, directed acyclic graph). Найдите его топологическую
сортировку, то есть выведите его вершины в таком порядке, что все рёбра графа идут слева направо. У графа может быть
несколько подходящих перестановок вершин. Вам надо найти любую топологическую сортировку.

Топологическая сортировка — это алгоритм, используемый для упорядочивания вершин в ориентированном ациклическом графе (
DAG) так, чтобы для каждого направленного ребра от вершины 𝑢 u к вершине v вершина u предшествовала вершине v
в порядке сортировки. Это означает, что если существует ребро u → v, то u должно быть расположено перед v.

Пример использования
Топологическая сортировка может быть полезна в различных областях, таких как:
Планирование задач: Определение порядка выполнения задач, где некоторые задачи зависят от завершения других.
Компиляция программного обеспечения: Установка зависимостей между модулями или библиотеками.
Упорядочивание учебных курсов: Определение последовательности прохождения курсов, где некоторые курсы требуют
предварительного изучения других.

Формат ввода
В первой строке даны два числа – количество вершин n (1 ≤ n ≤ 105) и количество рёбер m (0 ≤ m ≤ 105). В каждой из
следующих m строк описаны рёбра по одному на строке. Каждое ребро представлено парой вершин (from, to), 1≤ from, to ≤ n,
соответственно номерами вершин начала и конца.

Формат вывода
Выведите номера вершин в требуемом порядке.

"""

from collections import defaultdict


def adjacency_list(edge_list, n):
    adjacency_list = defaultdict(list)

    for u, v in edge_list:
        adjacency_list[u].append(v)

    for i in range(1, n + 1):
        if i not in adjacency_list:
            adjacency_list[i] = []
    return adjacency_list


def top_sort(color, v, adjacency_dict, stack):
    color[v] = "gray"

    for w in sorted(adjacency_dict[v]):
        if color[w] == 'white':
            top_sort(color, w, adjacency_dict, stack)
    color[v] = "black"
    stack.append(v)


def main_top_sort(n, color, adjacency_dict, stack):
    for i in adjacency_dict.keys():
        if color[i] == "white":
            top_sort(color, i, adjacency_dict, stack)


def main():
    n, m = tuple(map(int, (input().split(" ")))) # number vertex, number edge
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)]

    adjacency_dict = adjacency_list(edge_list, n)

    stack = []
    color = ["white"] * (n + 1)

    main_top_sort(n, color, adjacency_dict, stack)

    return " ".join(map(str, reversed(stack)))


if __name__ == "__main__":
    print(main())
