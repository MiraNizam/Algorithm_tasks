"""
B. Хеш-таблица

-- ПРИНЦИП РАБОТЫ --
Хеш-таблица реализована на массиве. Коллизии разрешаются метода цепочек, на основе связанных список. Максимально
допустимый размер 10^5, ближайшее простое число - 99997.  Принцип работы: на полученный ключ находим индекс, куда класть/
доставать/удалять. При возникновении коллизии, мы даем текущей паре (ключ, значение) ссылку на следующую и при
получении/добавлении/удалении проверяем вариант коллизии.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Работа данного алгоритма строится на работе с фиксированным массивом. Удаление, получение и добавление элементов идет
по индексам. Решение коллизий происходит на принципе связных списков.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
средняя временная сложность методов get, put, delete - О(1),
временная сложность методов в худшем случае get, put, delete - О(n), где n - количество элементов.

средняя сложность алгоритма с функцией main() - O(n), где n - количество запросов.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
средняя пространственная сложность - О(n), где n - размер фиксированного массива.

-- ID успешной посылки --
https://contest.yandex.ru/contest/24414/run-report/117273716/

"""


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}, {self.value}"


class HashTable:
    def __init__(self):
        self.size = 100007
        self.pairs = [None] * self.size

    def __hash_func(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.__hash_func(key)

        if self.pairs[index] is None:
            self.pairs[index] = Pair(key, value)
        else:
            pair = self.pairs[index]
            while pair:
                if pair.key == key:
                    pair.value = value
                    return
                if pair.next is None:
                    pair.next = Pair(key, value)
                    return
                pair = pair.next

    def get(self, key):
        index = self.__hash_func(key)
        pair = self.pairs[index]

        if self.pairs[index] is None:
            return None

        while pair:
            if pair.key == key:
                return pair.value
            pair = pair.next

    def delete(self, key):
        index = self.__hash_func(key)
        pair = self.pairs[index]

        if self.pairs[index] is None:
            return None

        previous = None
        while pair:
            if pair.key == key:
                if previous is None:
                    self.pairs[index] = pair.next
                else:
                    previous.next = pair.next
                return pair.value
            else:
                previous = pair
            pair = pair.next
        return None


def main():
    commands_n = int(input())
    new_hash_table = HashTable()
    for _ in range(commands_n):
        command = input()

        if command.startswith("get"):
            command, key = command.split(" ")
            print(new_hash_table.get(int(key)))

        elif command.startswith("put"):
            command, key, value = command.split(" ")
            new_hash_table.put(int(key), int(value))

        elif command.startswith("delete"):
            command, key = command.split(" ")
            print(new_hash_table.delete(int(key)))


if __name__ == "__main__":
    main()