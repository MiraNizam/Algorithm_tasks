"""
A. Мониторинг

Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.
Транспонированная матрица получается из исходной заменой строк на столбцы.

Формат ввода
В первой строке задано число n — количество строк матрицы.
Во второй строке задано m — число столбцов, m и n не превосходят 1000.
В следующих n строках задана матрица. Числа в ней не превосходят по модулю 1000.

Формат вывода
Напечатайте транспонированную матрицу в том же формате, который задан во входных данных.
Каждая строка матрицы выводится на отдельной строке, элементы разделяются пробелами.
"""

def matrix_transposition():
    # string_number = int(input())
    # column_number = int(input())
    N = 3
    M = 2
    row = [0] * M  # создаем список-строку длиной M
    A = [row] * N  # создаем массив (список) из N строк
    A[0][0] = 1

    # old_matrix = []
    # new_matrix = [[], []]
    # new_matrix[0][0] = 3
    print(A)
    # for _ in range(string_number):
    #     old_matrix.append(list(map(int, input().split(" "))))
    # print(old_matrix)
    # index = 0
    # for str in range(string_number):
    #     for col in range(column_number):
    #         print(old_matrix[str][col])
    #         new_matrix.append(old_matrix[str][col])
    #         # new_matrix[index].append(old_matrix[str][col])
    #         # print(new_matrix)




if __name__ == "__main__":
    matrix_transposition()