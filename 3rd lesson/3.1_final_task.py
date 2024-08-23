"""
-- ПРИНЦИП РАБОТЫ --

На вход поступает массив отсортированных уникальных числовых значений "сломанный после разрыва кольцевого буфера"
т.к. может быть сдвиг элементов. т.к. его части все равно отсортированы будем использовать принципы бинарного поиска,
разделение по срединному элементу и постепенное уменьшение диапазона проверяемых элементов.

- находим средний элемент, если он искомый, то возвращаем результат
- у нас 2 части массива, одна отсортирована, в другой части будут элементы сбиты.
- проверим каждую часть массива на отсортированность, находим отсортированную, проверяем подходит ли диапазон значений:
    - если не подходит, то уменьшаем значение сред.элемента и продолжаем поиск в другой части.
    - если подходит, то уменьшаем значение сред.элемента и продолжаем поиск в этой части.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Корректность следует, из того, что мы реализуем бинарный поиск, дополнительно у нас реализован только выбор
сортированной части.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Бинарный поиск работает за O(log n), поэтому общая сложность программы O(log n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
т.к.дополнительно мы не выделяем переменную под хранение массива и работаем только индексами и заданными значениями,
то пространственная сложность должна быть О(1)

-- ID успешной посылки --
https://contest.yandex.ru/contest/23815/run-report/116801719/
"""


def broken_search(nums, target) -> int:
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_element_index = (left_index + right_index) // 2

        if nums[mid_element_index] == target:
            return mid_element_index

        if nums[left_index] <= nums[mid_element_index]:
            if nums[left_index] <= target < nums[mid_element_index]:
                right_index = mid_element_index - 1
            else:
                left_index = mid_element_index + 1
        else:
            if nums[mid_element_index] < target <= nums[right_index]:
                left_index = mid_element_index + 1
            else:
                right_index = mid_element_index - 1
    return -1


def main():
    len_nums = int(input())
    target = int(input())
    nums = list(map(int, input().split(" ")))
    print(broken_search(nums, target))


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == "__main__":
    main()
    test()
