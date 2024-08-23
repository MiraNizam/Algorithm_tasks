"""
B. Соревнование
Жители Алгосов любят устраивать турниры по спортивному программированию. Все участники разбиваются на пары и соревнуются
друг с другом. А потом два самых сильных программиста встречаются в финальной схватке, которая состоит из нескольких
раундов. Если в очередном раунде выигрывает первый участник, в таблицу с результатами записывается 0, если второй, то 1.
 Ничьей в раунде быть не может.

Нужно определить наибольший по длине непрерывный отрезок раундов, по результатам которого суммарно получается ничья.
Например, если дана последовательность 0 0 1 0 1 1 1 0 0 0, то раунды с 2-го по 9-й (нумерация начинается с единицы)
дают ничью.

Формат ввода
В первой строке задаётся n (0 ≤ n ≤ 105) –— количество раундов. Во второй строке через пробел записано n чисел –— результаты раундов. Каждое число равно либо 0, либо 1.

Формат вывода
Выведите длину найденного отрезка.


"""


def competition():
    # nums = int(input())
    round_results = "110100110"
    current_score = 0 # текущий счет
    index_by_score = {0: -1}  # хеш-таблица счета и индекса, первый элемент счет равен 0, индекс -1
    max_length = 0 # максимальная длина

    for i, round in enumerate(round_results): # проходим по последовательности, если "1" то добавляет, если "0" отнимаем
        print(index_by_score)
        if round == "1":
            current_score += 1
        else:
            current_score -= 1

        if current_score in index_by_score: # ключами хеш-таблицы является счет, если ранее этот счет уже был,
            # то мы обновляем макс. длину отрезка т.к. это означает, что длина "ничьи" может измениться
            max_length = max(max_length, i - index_by_score[current_score])
            print(max_length)
        else:
            # если этого счета ранее не было, то сохраняем индекс, когда этот счет первый раз появился
            index_by_score[current_score] = i

    return max_length


if __name__ == "__main__":
    print(competition())


def competition():
    nums = int(input())
    round_results = input()
    current_score = 0
    index_by_score = {0: -1}
    max_length = 0

    for i, round in enumerate(round_results):
        if round == "1":
            current_score += 1
        else:
            current_score -= 1

        if current_score in index_by_score:
            max_length = max(max_length, i - index_by_score[current_score])
        else:
            index_by_score[current_score] = i

    return max_length


if __name__ == "__main__":
    print(competition())