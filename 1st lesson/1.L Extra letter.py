"""
L. Лишняя буква

Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

"""

def find_extra_letter():
    first_string = input()
    second_string = input()

    for letter in second_string:
        if letter not in first_string:
            return letter
        elif letter in first_string and first_string.count(letter) < second_string.count(letter):
            return letter



if __name__ == "__main__":
    print(find_extra_letter())