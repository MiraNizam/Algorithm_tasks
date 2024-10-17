"""
H. Глобальная замена

Напишите программу, которая будет заменять в тексте все вхождения строки s на строку t. Гарантируется, что никакие
два вхождения шаблона s не пересекаются друг с другом.

Формат ввода
В первой строке дан текст —– это строка из строчных букв английского алфавита, длина которой не превышает 106.

Во второй строке записан шаблон s, вхождения которого будут заменены.

В третьей строке дана строка t, которая будет заменять вхождения.

Обе строки s и t состоят из строчных букв английского алфавита, длина каждой строки не превосходит 105. Размер итоговой
строки не превосходит 2⋅ 106.

Формат вывода
В единственной строке выведите результат всех замен — текст, в котором все вхождения s заменены на t.
"""


def global_replacement(text, s, t, start_indices):
    result = list(text)

    offset = 0  # Смещение
    for index in start_indices:
        result[offset + index:offset + index + len(s)] = t
        offset += len(t) - len(s)

    return ''.join(result)


def search_substring_in_text(text, substring):
    s = f"{substring}#{text}"
    n = len(s)
    p = [None] * n
    p[0] = 0
    result = []

    for i in range(1, n):
        k = p[i - 1]

        while k > 0 and s[k] != s[i]:
            k = p[k - 1]

        if s[k] == s[i]:
            k += 1
        p[i] = k

        if k == len(substring):
            result.append(i - 2 * len(substring))
    return result


def main():
    text = input()
    substring = input()
    t = input()

    start_indices = search_substring_in_text(text, substring)
    result = global_replacement(text, substring, t, start_indices)

    print(result)


if __name__ == "__main__":
    main()