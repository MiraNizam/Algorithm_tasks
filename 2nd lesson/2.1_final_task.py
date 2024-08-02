"""
-- ПРИНЦИП РАБОТЫ --
Решение реализовано с помощью структуры данных Дек на кольцевом буфере. Представляет собой список элементов, в который
можно эффективно добавлять и удалять элементы с обоих концов, а кольцевой буфер представляет собой циклическую
реализацию, где есть ограничения по кол-ву элементов, т.к. задается максимальный размер и алгоритм будет сталкиваться с
переполнением, но преимуществом является экономия памяти для новых элементов.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания следует, что мы реализуем в принципы LIFO и FIFO. Мы сначала проверяем массив на достижение максимального
размера, после добавляем/удаляем по индексу в конец или начало.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
все операции дека на кольцевом буфере выполняются за O(1)
Общая сложность программы О(m), где m — максимальный размер дека

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
т.к.мы храним весь объем полученных данных в массиве для дальнейшей удобной обработки, то сложность будет О(m),
где m — максимальный размер дека

-- ID успешной посылки --
https://contest.yandex.ru/contest/22781/run-report/116509230/
"""


class MaxLimitError(Exception):
    def __str__(self):
        return "error"


class EmptyDequeError(Exception):
    def __str__(self):
        return "error"


class RingBufferDeque:
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = -1
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self.max_size:
            self.deque[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            raise MaxLimitError

    def push_front(self, x):
        if self.size != self.max_size:
            self.deque[self.head] = x
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            raise MaxLimitError

    def pop_back(self):
        if self.is_empty():
            raise EmptyDequeError
        else:
            self.tail = (self.tail - 1) % self.max_size
            x = self.deque[self.tail]
            self.deque[self.tail] = None
            self.size -= 1
            return x

    def pop_front(self):
        if self.is_empty():
            raise EmptyDequeError
        else:
            self.head = (self.head + 1) % self.max_size
            x = self.deque[self.head]
            self.deque[self.head] = None
            self.size -= 1
            return x


def limited_deque():
    command_no = int(input())
    max_size = int(input())
    new_deque = RingBufferDeque(max_size)
    for _ in range(command_no):
        command = input()
        try:
            if command.startswith("push_back"):
                command, number = command.split(" ")
                new_deque.push_back(int(number))
            elif command.startswith("push_front"):
                command, number = command.split(" ")
                new_deque.push_front(int(number))
            elif command.startswith("pop_back"):
                print(new_deque.pop_back())
            elif command.startswith("pop_front"):
                print(new_deque.pop_front())
        except MaxLimitError as error:
            print(error)
        except EmptyDequeError as error:
            print(error)


if __name__ == '__main__':
    limited_deque()
