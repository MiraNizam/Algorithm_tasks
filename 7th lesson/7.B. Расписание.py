"""
B. Расписание

Дано количество учебных занятий, проходящих в одной аудитории. Для каждого из них указано время начала и конца.
Нужно составить расписание, в соответствии с которым в классе можно будет провести как можно больше занятий.

Если возможно несколько оптимальных вариантов, то выведите любой. Возможно одновременное проведение более чем одного
занятия нулевой длительности.

Формат ввода
В первой строке задано число занятий. Оно не превосходит 1000. Далее для каждого занятия в отдельной строке записано
время начала и конца, разделённые пробелом. Время задаётся одним целым числом h, если урок начинается/заканчивается
ровно в h часов. Если же урок начинается/заканчивается в h часов m минут, то время записывается как h.m. Гарантируется,
что каждое занятие начинается не позже, чем заканчивается. Указываются только значащие цифры.

Формат вывода
Выведите в первой строке наибольшее число уроков, которое можно провести в аудитории. Далее выведите время начала и
конца каждого урока в отдельной строке в порядке их проведения.

Объяснить готовое решение можно так: чем раньше закончится мероприятие, тем больше времени для других встреч.
"""

def format_number(n):
    if n.is_integer():
        return int(n)
    else:
        return n

def schedule(n, lessons):
    sorted_lessons = sorted(lessons, key=lambda x: (float(x[1]), float(x[0])))
    schedule_list = [sorted_lessons[0]]
    for i in range(n-1):
        if sorted_lessons[i+1][0] >= schedule_list[-1][1]:
            schedule_list.append(sorted_lessons[i+1])
    print(len(schedule_list))
    for i in schedule_list:
        print(format_number(i[0]), format_number(i[1]))


def main():
    n = int(input())
    lessons = [(tuple(map(float, (input().split())))) for _ in range(n)]
    schedule(n, lessons)


if __name__ == "__main__":
    main()
