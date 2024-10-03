"""
B. Железные дороги

-- ПРИНЦИП РАБОТЫ --
строится на алгоритме DFS, который проверяет существует ли цикл в направленном графе. На основе карты ж/д дорог мы
строим лист смежности.
Из: ["BBB", "RB", "B"]
Получаем: [[], [0, 2], [0], [0, 1, 2]] если R, то прокладываем ребро от текущего города к городу-цели, если В,
то прокладываем ребро в обратном направлении. Обходим граф поиском в глубину, чтобы найти циклы.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
В основе решения лежит обход графов в глубину, алгоритм обходит все достижимые вершины графа, если во время обхода
находится соседняя вершина, которая в состоянии 1, то это указывает на наличие цикла и задача завершается, если нет,
то обход продолжается до последнего элемента.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(∣E∣ + ∣V∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(∣V∣), где ∣V∣ — количество вершин.

-- ID успешной посылки --
https://contest.yandex.ru/contest/25070/run-report/119557243/

"""


def dfs(vertex, adjacency, components):
    stack = [vertex]
    while stack:
        v = stack[-1]
        if components[v] == 0:
            components[v] = 1
            for neighbor in adjacency[v]:
                if components[neighbor] == 0:
                    stack.append(neighbor)
                elif components[neighbor] == 1:
                    return True
        else:
            components[v] = 2
            stack.pop()
    return False


def is_optimal(n, rail_map):
    city_count = n - 1
    adjacency = [[] for _ in range(n)]

    for i in range(city_count):
        for j in range(city_count - i):
            target_city = i + j + 1
            if rail_map[i][j] == "R":
                adjacency[i].append(target_city)
            elif rail_map[i][j] == "B":
                adjacency[target_city].append(i)
    components = [0] * len(adjacency)
    for vertex in range(len(adjacency)):
        if components[vertex] == 0 and dfs(vertex, adjacency, components):
            return "NO"
    return "YES"


def main():
    n = int(input())
    rail_map = [input() for _ in range(n-1)]
    return is_optimal(n, rail_map)


if __name__ == "__main__":
    print(main())

