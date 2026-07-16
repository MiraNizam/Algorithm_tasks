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
# 4 вершины, graph[i][j] = 1 если есть ребро i→j
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

обход бывает рекурсивный и итеративный
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
### **└── Union-Find / DSU (система непересекающихся множеств)**

## **Динамическое программирование**
### **├── Мемоизация (top-down, @lru_cache)**
### **├── Табличный DP (bottom-up)**
### **└── Классические паттерны (рюкзак, LCS, LIS, coin change)**


