# **Алгоритмы и структуры данных**
## **Массивы и строки**
### **├── Sliding Window (скользящее окно)**

Sliding Window нужен, когда тебе надо найти что-то оптимальное (максимум, минимум, количество) в непрерывном подмассиве или подстроке. Вместо того чтобы перебирать все пары индексов за O(N²), ты «тащишь» окно по массиву за O(N).
Фиксированное окно.

Видишь в условии что-то из этого — сразу думай про Sliding Window:
«подмассив/подстрока длины K»
«максимум/минимум среди всех подмассивов»
«не более K различных символов»
«наименьший подмассив с суммой ≥ X»

```
def sliding_window_fixed(arr, k):
    window = sum(arr[:k])
    best = window
    
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]  # сдвигаем: добавляем правый, убираем левый
        best = max(best, window)
    
    return best
```

Переменное окно:

```
def sliding_window_variable(arr, target):
    left = 0
    current = 0
    best = 0
    
    for right in range(len(arr)):
        current += arr[right]           # расширяем окно вправо
        
        while current > target:         # нарушено условие — сужаем слева
            current -= arr[left]
            left += 1
        
        best = max(best, right - left + 1)
    
    return best
```


### **├── Two Pointers (два указателя)**
Two Pointers нужен когда работаешь с отсортированным массивом и ищешь пару (или несколько) элементов с каким-то условием. Вместо двух вложенных циклов O(N²) — один проход O(N). Встречается в задачах на пары с суммой, палиндромы, удаление дубликатов.

Видишь в условии — думай про Two Pointers:

«отсортированный массив» + «найти пару»
«палиндром» (левый и правый идут навстречу)
«удалить дубликаты in-place»
«контейнер с водой» / «максимальная площадь»


```
def two_pointers(arr, target):
    # arr должен быть отсортирован!
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return (left, right)   # нашли пару
        elif s < target:
            left += 1              # сумма мала — двигаем левый вправо
        else:
            right -= 1             # сумма велика — двигаем правый влево

    return None


def max_water(height):
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        best = max(best, h * width)

        if height[left] < height[right]:
            left += 1   # левый меньше — двигаем его
        else:
            right -= 1  # правый меньше (или равны) — двигаем его

    return best
```


### **├── Prefix Sum (префиксные суммы)**
Нужен когда надо много раз считать сумму на отрезке [l, r]. Без префиксов каждый запрос — O(N). С префиксами — O(1) на запрос, O(N) на построение.

Сигналы к алгоритму:
«сумма на отрезке» / «несколько запросов к диапазону»
«количество подмассивов с суммой X» (prefix + hashmap)
«разность сумм двух частей»
```
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x
    return prefix

def range_sum(prefix, l, r):
    return prefix[r + 1] - prefix[l]  # сумма arr[l..r] включительно
    
или

def solve(arr, queries):
    # Строим prefix один раз — O(N)
    prefix = [0] * (len(arr) + 1)
    for i, x in enumerate(arr):
        prefix[i + 1] = prefix[i] + x

    # Каждый запрос — O(1)
    results = []
    for l, r in queries:
        results.append(prefix[r + 1] - prefix[l])
    return results

arr = [3, 1, 4, 1, 5, 9, 2, 6]
queries = [(0, 2), (1, 5), (3, 7)]
print(solve(arr, queries))  # [8, 20, 23]
    
```
count_subarrays:

```
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    seen = defaultdict(int)
    seen[0] = 1  # ← важно! пустой префикс с суммой 0 уже "видели" один раз

    for num in nums:
        prefix_sum += num
        # Ищем: сколько раз встречалась prefix_sum - k?
        count += seen[prefix_sum - k]
        # Фиксируем текущую префиксную сумму
        seen[prefix_sum] += 1

    return count
```

### **└── Counter / defaultdict / hashing**
 нужны, когда в задаче фигурируют фразы:
«частота элементов», «сколько раз встречается…»
«есть ли дубликаты», «найти элемент, который встречается ровно 1 раз»
«анаграммы», «сгруппировать по какому-то признаку»
Ты не пишешь вручную словарь и не проверяешь if key in dict, а сразу используешь готовые контейнеры из collections.
Counter — счётчик частот
```
from collections import Counter

arr = [1, 2, 2, 3, 3, 3]
freq = Counter(arr)
# freq: {1:1, 2:2, 3:3}  [web:23][web:41]
```
defaultdict — словарь с автоматическим значением
```
from collections import defaultdict

groups = defaultdict(list)       # значение по умолчанию — пустой список [web:38][web:24]

for word in ["eat", "tea", "tan", "ate", "nat", "bat"]:
    key = "".join(sorted(word))  # сортируем буквы: "aet", "ant", "abt"
    groups[key].append(word)

# groups = {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }
```

## **Поиск и сортировки**
### **├── Binary Search (бинарный поиск)**
сигналы: 
«отсортированный массив» + «найти элемент / границу»
«минимально/максимально возможное значение при условии»
«предикат монотонный» — то есть если значение X подходит, то X+1 тоже подходит (или наоборот)
```
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # не нашли
```
бинпоиск по ответу
```
def aggressive_cows(stalls: list, k: int) -> int:
    sorted_stalls = sorted(stalls)

    left, right = 1, sorted_stalls[-1] - sorted_stalls[0]
    best = 0
    while left <= right:
        mid = (left + right) // 2
        if can_place(stalls, k, mid):
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    return best

def can_place(stalls, k, d):
    placed_cows = 1
    last_placed = stalls[0]

    for x in stalls[1:]:
        if x - last_placed >= d:
            placed_cows += 1
            last_placed = x
            if placed_cows == k:
                return True
    return False
```

### **├── bisect (bisect_left, bisect_right)**
### **└── Custom Sort (сортировка с ключом/компаратором)**

## **Графы и деревья**
1. Список смежности (adjacency list) — самый популярный
```
# Ориентированный граф: 1→2, 1→3, 2→4, 3→4
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
2. Матрица смежности (adjacency matrix)

```
вершины, graph[i][j] = 1 если есть ребро i→j
```
graph = [
    [0, 1, 1, 0],  # вершина 0
    [0, 0, 0, 1],  # вершина 1
    [0, 0, 0, 1],  # вершина 2
    [0, 0, 0, 0],  # вершина 3
]
```
3. Список рёбер (edge list)
```
 edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
```
строишь список смежности
```
from collections import defaultdict

n, m = map(int, input().split())  # n вершин, m рёбер
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)          # ориентированный
    # graph[v].append(u)        # раскомментировать для неориентированного
```
Топологическая сортировка — это линейный порядок вершин ориентированного графа без циклов (DAG), 
Распознать задачу на граф

| Что написано в условии                   | Что это на самом деле              |
| ---------------------------------------- | ---------------------------------- |
| «N объектов», «M связей/зависимостей»    | Вершины и рёбра                    |
| «A зависит от B», «A нужно сделать до B» | Ориентированное ребро B → A        |
| «Можно перейти из A в B»                 | Ребро (может быть ориентированным) |
| «Найди порядок выполнения»               | Топологическая сортировка          |
| «Достижимо ли X из Y»                    | DFS/BFS обход                      |
| «Сколько групп/островов/компонент»       | Компоненты связности               |
| «Есть ли цикл/противоречие»              | Поиск цикла через DFS              |
Варианты задач:
1. Достижимость вершин
Тип задачи: «Можно ли добраться из A в B», «какие вершины достижимы из S».
2. Компоненты связности (сколько «островов»)
Тип задачи: «Сколько групп вершин, между которыми есть пути», «сколько связных компонент в графе».
```
components = 0

for v in range(1, n + 1):
    if not visited[v]:
        dfs(v)
        components += 1

print(components)
```
3. Поиск цикла
 3.1. Цикл в неориентированном графе
```
has_cycle = False
parent = [-1] * (n + 1)

def dfs(v):
    global has_cycle
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            parent[u] = v
            dfs(u)
        elif u != parent[v]:
            has_cycle = True
```
3.2. Цикл в ориентированном графе (раскраска)
```
import sys
from collections import defaultdict
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

WHITE, GRAY, BLACK = 0, 1, 2
color = [WHITE] * (n + 1)
has_cycle = False

def dfs(v):
    global has_cycle
    color[v] = GRAY
    for neighbor in graph[v]:
        if color[neighbor] == GRAY:
            has_cycle = True
            return
        if color[neighbor] == WHITE:
            dfs(neighbor)
    color[v] = BLACK

for v in range(1, n + 1):
    if color[v] == WHITE:
        dfs(v)

print("YES" if has_cycle else "NO")

```
4. Топологическая сортировка (Topsort)
Тип задачи: «Найти порядок выполнения задач/курсов/операций с зависимостями».
```
WHITE, GRAY, BLACK = 0, 1, 2
color = [WHITE] * (n + 1)
order = []
has_cycle = False

def dfs(v):
    global has_cycle
    color[v] = GRAY
    for u in graph[v]:
        if color[u] == GRAY:
            has_cycle = True
            return
        if color[u] == WHITE:
            dfs(u)
    color[v] = BLACK
    order.append(v)   # добавляем при выходе из вершины!

for v in range(1, n + 1):
    if color[v] == WHITE:
        dfs(v)

if has_cycle:
    print(-1)
else:
    print(*order[::-1])
```
5. Подсчёт чего-то по поддереву / компоненте
Например: «сколько вершин в этой компоненте», «какова сумма весов в этой группе».

```
def dfs_size(v):
    visited[v] = True
    size = 1
    for u in graph[v]:
        if not visited[u]:
            size += dfs_size(u)
    return size

component_sizes = []
for v in range(1, n + 1):
    if not visited[v]:
        component_sizes.append(dfs_size(v))

print(component_sizes)
```
6. Время входа/выхода (tin / tout)
```
timer = 0
tin = [0] * (n + 1)
tout = [0] * (n + 1)

def dfs(v):
    global timer
    visited[v] = True
    tin[v] = timer
    timer += 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
    tout[v] = timer
    timer += 1
```
7. Мосты и точки сочленения (шарниры)

### **├── DFS (обход в глубину)**

обход бывает рекурсивный (примеры выше и ниже)

итеративный:

def dfs_iterative(graph: dict, start: str) -> set:
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()          # достаём сверху (LIFO!)
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited


```
import sys
from collections import defaultdict
sys.setrecursionlimit(200000)
input = sys.stdin.readline          # быстрый ввод, важно на контестах

# === ЧТЕНИЕ ГРАФА (всегда одно и то же) ===
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    # graph[v].append(u)  # раскомментировать если граф НЕориентированный

# === DFS С РАСКРАСКОЙ (всегда одна и та же структура) ===
WHITE, GRAY, BLACK = 0, 1, 2
color = [WHITE] * (n + 1)
order = []
has_cycle = False

def dfs(v):
    global has_cycle
    color[v] = GRAY
    for u in graph[v]:
        if color[u] == GRAY:
            has_cycle = True
            return
        if color[u] == WHITE:
            dfs(u)
    color[v] = BLACK
    order.append(v)           # ← меняй эту строку под задачу

for v in range(1, n + 1):
    if color[v] == WHITE:
        dfs(v)

# === ОТВЕТ (зависит от задачи) ===
if has_cycle:
    print(-1)
else:
    print(*order[::-1])
   
```
| Задача           | Граф      | Что добавляется к базовому DFS                       |
| ---------------- | --------- | ---------------------------------------------------- |
| Достижимость     | ори/неори | ничего — просто visited[t] после запуска из s        |
| Компоненты       | неори     | счётчик запусков + graph[v].append(u)                |
| Размер компонент | неори     | dfs возвращает size, суммируем size += dfs(neighbor) |
| Цикл (неори)     | неори     | parent + elif u != parent                            |
| Цикл (ори)       | ори       | color WHITE/GRAY/BLACK + проверка на GRAY            |
| Топосорт         | ори, DAG  | color + order.append(v) при выходе + order[::-1]     |


### **├── BFS (обход в ширину)**
DFS использует стек (или рекурсию — это и есть стек).
BFS использует очередь (queue, FIFO — первый пришёл, первый вышел).
Главная суперсила BFS — кратчайшее расстояние
BFS гарантирует: когда мы впервые достигаем вершины t — мы прошли минимальное количество рёбер
from collections import deque

visited = [False] * (n + 1)

def bfs(s):
    queue = deque([s])      # очередь, стартуем из s
    visited[s] = True

    while queue:
        v = queue.popleft() # берём СЛЕВА (FIFO, не pop()!)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

BFS - поиск кратчайшего расстояния
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, m, s, t = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)    # граф двусторонний

def bfs(s):
    dist = [-1] * (n + 1)
    dist[s] = 0
    queue = deque([s])

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            # твой код

    return dist

dist = bfs(s)
print(dist[t])

BFS на сетке. Немного другой граф: вершины — это клетки, а не пронумерованные вершины 1..N.
```
from collections import deque

n, m = map(int, input().split())
sx, sy = map(int, input().split())
fx, fy = map(int, input().split())
grid = [input().strip() for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
dist[sx][sy] = 0
queue = deque([(sx, sy)])

directions = [(-1,0), (1,0), (0,-1), (0,1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "." and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(dist[fx][fy])
```
### **└── Union-Find / DSU (система непересекающихся множеств)**
Сложность
Amortized почти O(1) на операцию, благодаря сжатию пути и union by rank; память O(n) на массивы parent и rank.

Сигналы в условии
Ищи фразы: «объединить группы/друзей/компании», «проверить, принадлежат ли два элемента одной компоненте», «количество компонент меняется по ходу решения», «динамическая связность», «минимальное остовное дерево (Kruskal)».


from collections import defaultdict
n, m = map(int, input().split())


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.components = n
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1
        self.components -= 1

dsu = DSU(n)
for _ in range(m):
    u, v = map(int, input().split())
    dsu.union(u, v)
    max_values = max(dsu.size[dsu.find(v)] for v in range(1, n + 1))
    print(dsu.components, max_values)

## **Динамическое программирование**
Универсальный алгоритм: как писать DP с нуля
Когда видишь задачу, которая пахнет DP, пройди по этим 4 вопросам по порядку:

Что такое "состояние"? Какими параметрами описывается подзадача? (В лестнице — это просто номер ступеньки n. В более сложных задачах может быть пара (индекс, остаток_веса) и т.п.)

Какой базовый случай? Самая маленькая подзадача, ответ на которую ты знаешь без вычислений (n == 0 → 1 способ).

Как выразить большую подзадачу через меньшие? Это и есть рекуррентное соотношение — обычно отвечает на вопрос "какой был последний шаг/выбор?".

Оборачиваешь рекурсию в @lru_cache — и получаешь готовое DP-решение.
Весь секрет DP — не в коде, а в шаге 3. Как только ты нашёл правильное рекуррентное соотношение, код почти пишется сам.
### **├── Мемоизация (top-down, @lru_cache)**
DP нужен, когда задача сводится к рекурсии, но одни и те же подзадачи считаются много раз — мемоизация просто запоминает результат, чтобы не пересчитывать.
В Python это реализуется декоратором @lru_cache (Least Recently Used Cache) из модуля functools
Важно: аргументы dp должны быть неизменяемыми (int, tuple, str) — списки и словари lru_cache не хэширует.
maxsize=None убирает лимит кэша — на контестах это почти всегда правильный выбор, иначе можно неожиданно "вымыть" нужные значения из LRU-кэша при большом количестве вызовов.
```
from functools import lru_cache
import sys
sys.setrecursionlimit(300000)

@lru_cache(maxsize=None)
def dp(i, *state):
    if i == 0:
        return base_value  # базовый случай
    
    result = min(dp(i - 1, ...), dp(i - 1, ...))  # переходы
    return result

answer = dp(n, initial_state)
dp.cache_clear()  # если нужно освободить память между тестами

Сложность
O(число уникальных состояний × работа на переход), память O(число уникальных состояний) — потому что каждое состояние считается ровно один раз и кэшируется.

Сигналы в условии
«Рекурсия с повторяющимися подзадачами», «сколько способов сделать X», формулировка задачи естественно ложится на «выбор на каждом шаге» — легче думать сверху вниз, чем сразу строить таблицу.

```
### **├── Табличный DP (bottom-up)**
Нужно что-то максимизировать/минимизировать (сумма, количество способов, стоимость).
Решение явно строится из более мелких подзадач.
Наивная рекурсия считает одно и то же много раз → дерево вызовов раздувается.
Если видишь «последовательность выбора» (брать/не брать, идти туда/сюда, делать/не делать) — почти всегда там либо greedy, либо DP.
Tabulation (bottom-up)
def ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
### **└── Классические паттерны (рюкзак, LCS, LIS, coin change)**
text1 = "abcde"
text2 = "ace"

def lcs(text1, text2):
    """найти подпоследовательность. Состояние dp[i][j] это длина общей подпоследовательности """
    len1 = len(text1)
    len2 = len(text2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len1][len2]


def edited_distance(text1, text2):
    """сколько нужно изменений чтобы превратить слово1 в слово2. dp[i][j] кол-во изменений в подстроке"""
    len1 = len(text1)
    len2 = len(text2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[len1][len2]


