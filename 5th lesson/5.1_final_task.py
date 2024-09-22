"""
A. Пирамидальная сортировка

-- ПРИНЦИП РАБОТЫ --
алгоритм строится на работе бинарной кучи. Создаем пустую бинарную невозрастающую кучу (mах-heap), добавляем туда
элементы согласно главному свойству бинарной кучи: родительский элемент больше дочерних, а на вершине, максимальный
элемент. Удаляем вершину (максимальный элемент) и перестраиваем кучу по свойствам, продолжаем вытаскивать приоритетные
элементы пока куча не закончилась.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
В основе алгоритма лежит бинарная куча на массиве и реализованная с ее помощью пирамидальная сортировка.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

В худшем случае временная сложность вставки происходит за О(logn) - высота кучи
В худшем случае временная сложность удаления происходит за О(logn) - высота кучи
В худшем случае временная сложность сортировки - О(nlogn)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Пространственная сложность - О(n), где n - массив элементов.

-- ID успешной посылки --
https://contest.yandex.ru/contest/24810/run-report/118527306/

"""

def check_swap(heap, index, parent_index):
    if index >= len(heap) or parent_index >= len(heap):
        return False

    if heap[index][1] > heap[parent_index][1]:
        return True
    elif heap[index][1] == heap[parent_index][1] and heap[index][2] < heap[parent_index][2]:
        return True
    elif heap[index][1] == heap[parent_index][1] and heap[index][2] == heap[parent_index][2] and heap[index][0] < heap[parent_index][0]:
        return True
    return False


def get_largest_index(left, right, heap, index):
    heap_max_index = len(heap) - 1
    largest = index

    if left <= heap_max_index and check_swap(heap, left, largest):
        largest = left

    if left <= heap_max_index and check_swap(heap, right, largest):
        largest = right

    return largest


def sift_up(heap, index):
    if index == 0:
        return

    parent_index = (index - 1) // 2

    if check_swap(heap, index, parent_index):
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        sift_up(heap, parent_index)


def heap_add(heap, i):
    heap.append(i)
    index = len(heap) - 1
    sift_up(heap, index)


def sift_down(heap, index):
    left = index * 2 + 1
    right = index * 2 + 2

    largest = get_largest_index(left, right, heap, index)

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        sift_down(heap, largest)


def pop_max(heap):
    result = heap[0]
    if len(heap) == 1:
        heap.pop()
        return result
    heap[0] = heap[-1]
    heap.pop()
    sift_down(heap, 0)
    return result


def pyramid_sort(unsorted_massive):
    max_heap = []
    for i in unsorted_massive:
        heap_add(max_heap, i)
    sorted_arr = []
    while len(max_heap) > 0:
        max_val = pop_max(max_heap)
        sorted_arr.append(max_val)

    return sorted_arr


def main():
    n = int(input())
    participants = [(name, int(tasks), int(penalty)) for name, tasks, penalty in
                    (input().split(" ") for _ in range(n))]

    sorted_participants = pyramid_sort(participants)

    for participant in sorted_participants:
        print(participant[0])


if __name__ == "__main__":
    main()