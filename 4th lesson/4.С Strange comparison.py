"""
C. Странное сравнение


Жители Алгосского архипелага придумали новый способ сравнения строк. Две строки считаются равными, если символы одной
из них можно заменить на символы другой так, что первая строка станет точной копией второй строки. При этом необходимо
соблюдение двух условий:

Порядок вхождения символов должен быть сохранён.
Одинаковым символам первой строки должны соответствовать одинаковые символы второй строки.
Разным символам —– разные.
Например, если строка s = «abacaba», то ей будет равна строка t = «xhxixhx»,
так как все вхождения «a» заменены на «x», «b» –— на «h», а «c» –— на «i».
Если же первая строка s=«abc», а вторая t=«aaa», то строки уже не будут равны, так как разные буквы первой строки
соответствуют одинаковым буквам второй.

Формат ввода
В первой строке записана строка s, во второй –— строка t. Длины обеих строк не превосходят 10^6.
Обе строки содержат хотя бы по одному символу и состоят только из маленьких латинских букв.

Строки могут быть разной длины.

Формат вывода
Выведите «YES», если строки равны (согласно вышеописанным правилам), и «NO» в ином случае.


"""


def strange_comparison():
    s, t = input(), input()

    if len(s) != len(t):
        return "NO"
    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        if s[i] not in dict_s:
            dict_s[s[i]] = t[i]
        elif dict_s[s[i]] != t[i]:
            return "NO"

        if t[i] not in dict_t:
            dict_t[t[i]] = s[i]
        elif dict_t[t[i]] != s[i]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    print(strange_comparison())