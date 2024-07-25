"""
-- ПРИНЦИП РАБОТЫ --
-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
-- ID успешной посылки --

"""

class RingBufferDeque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.head == 0 and self.tail == 0:
            self.head = -1
        if self.size != self.max_size:
            self.deque[self.tail] = x # error
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            print(self.deque, self.head, self.tail)
        else:
            print("error")

    def push_front(self, x):
        if self.head == 0 and self.tail == 0:
            self.tail = 1
        if self.size != self.max_size:
            self.deque[self.head] = x # error
            self.head = (self.head - 1) % self.max_size
            self.size += 1
            print(self.deque, self.head, self.tail)
        else:
            print("error")

    def pop_back(self):
        if self.is_empty():
            print("error")
        else:
            self.tail = (self.tail - 1) % self.max_size
            x = self.deque[self.tail]
            self.deque[self.tail] = None
            self.size -= 1
            if self.is_empty():
                self.tail = self.head = 0
            print(x)

    def pop_front(self):
        if self.is_empty():
            print("error")
        else:
            self.head = (self.head + 1) % self.max_size
            x = self.deque[self.head]
            self.deque[self.head] = None
            self.size -= 1
            if self.is_empty():
                self.tail = self.head = 0
            print(x)


def limited_deque():
    command_no = int(input())
    max_size = int(input())
    new_deque = RingBufferDeque(max_size)
    for _ in range(command_no):
        command = input()
        if command.startswith("push_back"):
            command, number = command.split(" ")
            new_deque.push_back(int(number))
        elif command.startswith("push_front"):
            command, number = command.split(" ")
            new_deque.push_front(int(number))
        elif command.startswith("pop_back"):
            new_deque.pop_back()
        elif command.startswith("pop_front"):
            new_deque.pop_front()


if __name__ == '__main__':
    limited_deque()
