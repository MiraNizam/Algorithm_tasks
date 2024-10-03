"""
A. Дорогая сеть
Задача создать максимальное остовное дерево

-- ПРИНЦИП РАБОТЫ --
Создаем класс Граф, граф в нем будет представлен в виде листа смежности, с указанием количества вершин и ребер.
Реализуем в классе два метода, добавление вершин в лист смежности и создание максимального остовного дерева. Подробнее
про создание макс. остовного дерева.
Первое, необходимо оптимально отбирать ребра с максимальными весами, для этого используется куча с приоритетом.
Заводим множество для хранения посещенных вершин, чтобы не повторятся.
И заводим список для макс. остовного дерева.
Начинаем с первой вершины, можно с любой. Добавляем в кучу все ребра для этой вершины (куча сортирует элементы так, что
мы заберем оттуда максимальное по весу ребро). В цикле мы забираем из кучи максимальный по весу элемент, идем в следующую
вершину, проверяем была ли она ранее посещена, если да, то пропускаем, такое ребро нам не нужно. Если ранее не посещали
мы пополняем список макс. остовного дерева и проверяем следующую вершину, добавляем в кучу ее ребра и проверяем по циклу

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
В основе решения задачи лежит Алгоритм Прима на очереди с поддержанием максимума.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

O(∣E∣⋅log∣V∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

O(∣V∣ + ∣E∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.

-- ID успешной посылки --
https://contest.yandex.ru/contest/25070/run-report/119374717/

"""

import heapq
from collections import defaultdict


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def find_maxst(self):
        max_heap = []
        visited = set()
        maximum_spanning_tree = []

        start_vertex = 1
        visited.add(start_vertex)

        for neighbour, weight in self.graph[start_vertex]:
            heapq.heappush(max_heap, (-weight, start_vertex, neighbour))

        while max_heap:
            weight, u, v = heapq.heappop(max_heap)
            weight = -weight

            if v not in visited:
                visited.add(v)
                maximum_spanning_tree.append((u, v, weight))

                for next_neighbour, next_weight in self.graph[v]:
                    if next_neighbour not in visited:
                        heapq.heappush(max_heap, (-next_weight, v, next_neighbour))

        return maximum_spanning_tree, len(visited)

    def __str__(self):
        return f"{self.graph}"


def main():
    n, m = tuple(map(int, (input().split(" ")))) # количество вершин, количество ребер
    edge_list = [list(map(int, (input().split(" ")))) for _ in range(m)] # u, v, w. u и v — вершины, которые соединяет это ребро. w — его вес

    graph = Graph(n, m)

    for u, v, w in edge_list:
        graph.add_edge(u, v, w)
    maximum_spanning_tree, visited_count = graph.find_maxst()
    if visited_count != n:
        return "Oops! I did it again"

    total_weight = sum(weight for _, _, weight in maximum_spanning_tree)
    return total_weight


if __name__ == "__main__":
    print(main())

