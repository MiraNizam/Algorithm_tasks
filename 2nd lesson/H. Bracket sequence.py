"""
H. Скобочная последовательность

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:
пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа, –— правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True, если последовательность правильная, а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.

Формат вывода
Выведите «True» или «False».
"""

def is_correct_bracket_seq():
    bracket_seq = input()
    if len(bracket_seq) == 0:
        return True
    bracket_couples = {"}": "{", ")": "(", "]": "["}
    open_brackets = ["{", "(", "["]
    bracket_seq_new = []
    for bracket in bracket_seq:
        if bracket in open_brackets:
            bracket_seq_new.append(bracket)
        else:
            if bracket_seq_new and bracket_couples[bracket] == bracket_seq_new[-1]:
                bracket_seq_new.pop()
            else:
                return False
    if len(bracket_seq_new) == 0:
        return True
    return False

if __name__ == '__main__':
    print(is_correct_bracket_seq())