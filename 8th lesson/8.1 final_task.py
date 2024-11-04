"""
A. Packed Prefix

Вам даны строки в запакованном виде. Определим запакованную строку (ЗС) рекурсивно. Строка, состоящая только из строчных
букв английского алфавита является ЗС. Если A и B —– корректные ЗС, то и AB является ЗС. Если A —– ЗС, а n — однозначное
натуральное число, то n[A] тоже ЗС. При этом запись n[A] означает, что при распаковке строка A записывается подряд n раз
. Найдите наибольший общий префикс распакованных строк и выведите его (в распакованном виде).

Формат ввода
В первой строке записано число n (1 ≤ n ≤ 1000) –— число строк.

Далее в n строках записаны запакованные строки. Гарантируется, что эти строки корректны, то есть удовлетворяют
указанному рекурсивному определению. Длина строк после распаковки не превосходит 105.


-- ПРИНЦИП РАБОТЫ --
Решение состоит из двух частей: функция recursive_unpack, распаковывает рекурсивно запакованные строки; функция
longest_common_prefix ищет наибольший общий префикс, за префикс берем первую строку и сравниваем строки поочередно с
первым элементом(префиксом), если они не совпадают, уменьшаем длину префикса и повторяем.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
в основе решения задачи лежит рекурсия для распаковки строк и метод последовательного сравнения строк, который сокращает
префикс до совпадения с остальными строками. Это гарантирует, что мы найдем наиб.общий префикс.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(nk), где n - количество строк, k - максимальная длина распакованной строки.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(n), где n - распакованные строки

-- ID успешной посылки --
https://contest.yandex.ru/contest/26133/run-report/123188263/

"""


def recursive_unpack(packed_str: str, index: int) -> tuple:
    unpacked_string = ""
    number = 0

    while index < len(packed_str):
        symbol = packed_str[index]

        if symbol.isdigit():
            number = int(symbol)
        elif symbol == "[":
            inner_string, index = recursive_unpack(packed_str, index + 1)
            unpacked_string += inner_string * (number if number > 0 else 1)
            number = 0
        elif symbol == "]":
            return unpacked_string, index
        else:
            unpacked_string += symbol
        index += 1
    return unpacked_string, index


def longest_common_prefix(strs: list) -> str:
    prefix = strs[0]
    for str in strs[1:]:
        while str[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

    return prefix


def main() -> str:
    n = int(input())
    strs = [input() for _ in range(n)]
    unpacked_strings = []
    for str in strs:
        unpacked_str, index = recursive_unpack(str, 0)
        unpacked_strings.append(unpacked_str)

    common_prefix = longest_common_prefix(unpacked_strings)

    return common_prefix


if __name__ == "__main__":
    print(main())
