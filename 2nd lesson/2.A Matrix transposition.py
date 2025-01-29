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


# def matrix_transposition(string_number, column_number, matrix):
#     new_matrix = [[0 for _ in range(string_number)] for _ in range(column_number)]
#     print(new_matrix)
#     for i in range(string_number):
#         print(i)
#         for j in range(column_number):
#             print(j)
#             new_matrix[j][i] = matrix[i][j]
#     print(new_matrix)
#
#
# if __name__ == "__main__":
#     string_number = int(input())
#     column_number = int(input())
#     matrix = [input().split(' ') for j in range(string_number)]
#     matrix_transposition(string_number, column_number, matrix)
#


def matrix_transposition():
    string_number = int(input())
    column_number = int(input())
    old_matrix = [input().split(' ') for j in range(string_number)]

    for i in range(column_number):
        for j in range(string_number):
            print(old_matrix[j][i], end=' ')
        print('')


if __name__ == "__main__":
    matrix_transposition()