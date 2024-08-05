"""
J. Пузырёк
На очереди сортировка пузырьком — https://ru.wikipedia.org/wiki/Сортировка_пузырьком

Её алгоритм следующий (сортируем по неубыванию):

На каждой итерации проходим по массиву, поочередно сравнивая пары соседних элементов. Если элемент на позиции i больше
элемента на позиции i + 1, меняем их местами. После первой итерации самый большой элемент всплывёт в конце массива.
Проходим по массиву, выполняя указанные действия до тех пор, пока на очередной итерации не окажется, что обмены больше
не нужны, то есть массив уже отсортирован.
После не более чем n – 1 итераций выполнение алгоритма заканчивается, так как на каждой итерации хотя бы один элемент
оказывается на правильной позиции.
"""

massive_len = int(input())
massive = list(map(int, input().split(" ")))


def bubble_sort(massive_len, massive):
    if all(massive[i] <= massive[i+1] for i in range(massive_len-1)):
        print(" ".join([str(n) for n in massive]))

    stage = massive_len - 1
    while stage > 0:
        changes = 0
        for i in range(1, massive_len):
            if massive[i] < massive[i - 1]:
                massive[i - 1], massive[i] = massive[i], massive[i - 1]
                changes += 1
        if changes == 0:
            break
        stage -= 1
        print(" ".join([str(n) for n in massive]))


if __name__ == "__main__":
    bubble_sort(massive_len, massive)

