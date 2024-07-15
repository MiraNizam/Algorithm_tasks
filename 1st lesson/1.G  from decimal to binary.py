"""
G. Из десятичной в двоичную

Переводит целое число из десятичной системы в двоичную.

Не используйте встроенные средства языка по переводу чисел в бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.

"""


def from_decimal_to_binary():
    decimal_number = int(input())
    x = decimal_number
    binary_number = ""
    if decimal_number == 0:
        return 0
    while x > 0:
        binary_number = str(x % 2) + binary_number
        x = x // 2
    return binary_number


if __name__ == '__main__':
    print(from_decimal_to_binary())
