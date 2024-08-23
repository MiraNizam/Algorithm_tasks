"""
A. Кружки
Когда кто-то записывается на занятие, в лог вносится название кружка.

По записям в логе составьте список всех кружков, в которые ходит хотя бы один человек.
"""


def hobby_list():
    nums = int(input())
    hobbies = {}
    for _ in range(nums):
        hobby = input()
        if hobby not in hobbies:
            hobbies[hobby] = 1
            print(hobby)
        else:
            hobbies[hobby] += 1


if __name__ == "__main__":
    hobby_list()