"""
C. Подпоследовательность

Даны 2 строки, и нужно понять, является ли первая из них подпоследовательностью второй.

Формат ввода
В первой строке записана строка s.

Во второй —- строка t.

Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки не могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.

"""

# s = str(input()) # подпоследовательность
# t = str(input())


def is_subsequence(s, t):
    last_index = 0
    for letter in s:
        print(last_index, letter)
        position = t.find(letter, last_index)
        if position != -1:
            last_index = position + 1
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    s = "aab"
    t = "abb"
    print(is_subsequence(s, t))