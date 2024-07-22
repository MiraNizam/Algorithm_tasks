"""
F. Стек - Max

Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не превосходит 10000. В следующих n строках идут команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек. Число x не превышает 105;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».
"""

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print("error")

    def get_max(self):
        if self.items:
            print(max(self.items))
        else:
            print("None")


def work_stack_max():
    no_commands = int(input())
    new_stack = StackMax()
    for _ in range(no_commands):
        command = input()

        if command.startswith("push"):
            command, number = command.split(" ")
            new_stack.push(int(number))

        elif command.startswith("pop"):
            new_stack.pop()
        elif command.startswith("get_max"):
            new_stack.get_max()

if __name__ == '__main__':
    work_stack_max()