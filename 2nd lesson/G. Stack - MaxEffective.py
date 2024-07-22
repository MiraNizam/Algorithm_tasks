"""
G. Стек - MaxEffective

Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000. Далее идут команды по одной в
строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек. Число x не превышает 105;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
top() — напечатать число с вершины стека;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop и top — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте
«None». Если происходит удаление из пустого стека — напечатайте «error».
"""



class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            if item > self.items[-1][1]:
                maximum = item
                self.items.append((item, maximum))
            else:
                self.items.append((item, self.items[-1][1]))
        else:
            maximum = item
            self.items.append((item, maximum))

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print("error")

    def get_max(self):
        if self.items:
            print(self.items[-1][1])
        else:
            print("None")

    def top(self):
        if self.items:
            print(self.items[-1][0])
        else:
            print("error")


def work_stack_max():
    no_commands = int(input())
    new_stack = StackMaxEffective()
    for _ in range(no_commands):
        command = input()

        if command.startswith("push"):
            command, number = command.split(" ")
            new_stack.push(int(number))
        elif command.startswith("pop"):
            new_stack.pop()
        elif command.startswith("get_max"):
            new_stack.get_max()
        elif command.startswith("top"):
            new_stack.top()


if __name__ == '__main__':
    work_stack_max()