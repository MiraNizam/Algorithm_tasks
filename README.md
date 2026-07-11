``Массивы и строки``
├── Sliding Window (скользящее окно)

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


├── Two Pointers (два указателя)
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


├── Prefix Sum (префиксные суммы)
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

└── Counter / defaultdict / hashing
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

Поиск и сортировки
├── Binary Search (бинарный поиск)
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
├── bisect (bisect_left, bisect_right)
└── Custom Sort (сортировка с ключом/компаратором)

Графы и деревья
├── DFS (обход в глубину)
├── BFS (обход в ширину)
└── Union-Find / DSU (система непересекающихся множеств)

Динамическое программирование
├── Мемоизация (top-down, @lru_cache)
├── Табличный DP (bottom-up)
└── Классические паттерны (рюкзак, LCS, LIS, coin change)


