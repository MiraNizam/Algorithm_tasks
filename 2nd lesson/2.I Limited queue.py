"""
I. Ограниченная очередь

нужно написать класс MyQueueSized, который принимает параметр max_size, означающий максимально допустимое количество элементов в очереди.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.
"""

class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def pop(self):
        if self.is_empty():
            print(None)
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            print(x)

    def peek(self):
        if self.is_empty():
            print(None)
        else:
            print(self.queue[self.head])

    def queue_size(self):
        print(self.size)


def limited_queue():
    command_no = int(input())
    max_size = int(input())
    new_queue = MyQueueSized(max_size)
    for _ in range(command_no):
        command = input()
        if command.startswith("push"):
            command, number = command.split(" ")
            new_queue.push(int(number))
        elif command.startswith("pop"):
            new_queue.pop()
        elif command.startswith("peek"):
            new_queue.peek()
        elif command.startswith("size"):
            new_queue.queue_size()


if __name__ == '__main__':
    limited_queue()