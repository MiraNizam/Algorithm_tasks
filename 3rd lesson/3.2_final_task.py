"""
-- ПРИНЦИП РАБОТЫ --
Решение реализовано с помощью принципов Quicksort, на основе рекурсии.
Выбираем рандомный элемент в качестве опорного, переносим в крайнее правое положение.
Проходим циклом по массиву, если элемент меньше опорного, меняем его с крайним левым элементом массива, перенося индекс
на следующий элемент. Последним переносим опорный элемент, закрывая т.о. первый уровень быстрой сортировки.
Следующие уровни будут вызваны рекурсией, а новыми границами сортируемых отрезков массивов будут опорные элементы.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует, что мы реализуем Quicksort, отличие от классической версии, что не выделяем отрезки на каждом
уровне рекурсии, а перемещаем внутри заданного массива, перемещения выполняются согласно принципам быстрой сортировки,
относительно рандомного опорного элемента.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
тут ничего не должно было измениться от классической Quicksort, поэтому временная сложность в среднем случае O(nlogn),
в худшем случае O(n^2)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
предполагаю, что пространственная может расходоваться только на рекурсию и тогда сложность будет O(logn)

-- ID успешной посылки --
https://contest.yandex.ru/contest/23815/run-report/116878969/
"""


import random


def partition(array, index_left, index_right, key):
    pivot = array[index_right]
    moving_index = index_left

    for i in range(index_left, index_right):
        if key(array[i]) < key(pivot):
            array[moving_index], array[i] = array[i], array[moving_index]
            moving_index += 1

    array[moving_index], array[index_right] = array[index_right], array[moving_index]
    return moving_index


def quick_sort_in_place(array, index_left, index_right, key):
    if index_left < index_right:

        random_index = random.randint(index_left, index_right)
        array[random_index], array[index_right] = array[index_right], array[random_index]
        pivot_index = partition(array, index_left, index_right, key)

        quick_sort_in_place(array, index_left, pivot_index-1, key)
        quick_sort_in_place(array, pivot_index+1, index_right, key)


if __name__ == "__main__":
    nums = int(input())
    participants = [[name, int(tasks), int(penalty)] for name, tasks, penalty in (input().split(" ") for _ in range(nums))]

    index_left = 0
    index_right = nums-1
    quick_sort_in_place(participants, index_left, index_right, key=lambda participant: [-participant[1], participant[2], participant[0]])
    for participant in participants:
        print(participant[0])
