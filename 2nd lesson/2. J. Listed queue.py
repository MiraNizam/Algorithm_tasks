"""
J. Списочная очередь

очередь, написанная с использованием связного списка. Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class ListedQueue:
    def __init__(self, value=None):
        self.head = None # если список пуст, мы добавляем сюда значение. Если удаляем, то меняем на следующее
        self.node = None # при добавлении
        self.size = 0 # счетчик

    def get(self):
        if self.size == 0:
            print("error")
        else:
            self.size -= 1
            deleted_element = self.head
            print(deleted_element)
            self.head = deleted_element.next

    def put(self, new_element):
        new_node = Node(new_element)
        self.size += 1

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def qsize(self):
        print(self.size)

def limited_queue():
    command_no = int(input())
    new_queue = ListedQueue()
    for _ in range(command_no):
        command = input()
        if command.startswith("put"):
            command, number = command.split(" ")
            new_queue.put(int(number))
        elif command.startswith("get"):
            new_queue.get()
        elif command.startswith("size"):
            new_queue.qsize()


if __name__ == '__main__':
    limited_queue()

