"""
F. Палиндром

Будет ли фраза палиндромом. Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.


"""


def palindrom():
    phrase = list(input().lower())
    upgrade_phrase = phrase.copy()

    first_index = 0
    last_index = len(upgrade_phrase)-1

    while last_index > first_index:
        upgrade_phrase[first_index], upgrade_phrase[last_index] = upgrade_phrase[last_index], upgrade_phrase[first_index]
        last_index -= 1
        first_index += 1

    if upgrade_phrase == phrase:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    palindrom()
