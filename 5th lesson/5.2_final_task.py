"""
B. Удали узел

Дано бинарное дерево поиска, в котором хранятся ключи. Ключи — уникальные целые числа. Найдите вершину с заданным ключом
и удалите её из дерева так, чтобы дерево осталось корректным бинарным деревом поиска. Если ключа в дереве нет, то
изменять дерево не надо.
На вход вашей функции подаётся корень дерева и ключ, который надо удалить. Функция должна вернуть корень изменённого
дерева. Сложность удаления узла должна составлять O(h), где h –— высота дерева.
Создавать новые вершины (вдруг очень захочется) нельзя.

-- ПРИНЦИП РАБОТЫ --
в основе лежит удаление элемента по заданному ключу из бинарного дерева. Удаление происходит так: рекурсивно спускаемся
по дереву сравнивая левый и правый узлы на каждом уровне. Когда находим и у элемента оказывается только один дочерний
узел, ставим его на место удаленного элемента, если у элемента два дочерних узла мы ищем минимальный правый элемент
(также можно искать максимальный левый) и заполняем им место удаленного узла.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Алгоритм строится на двоичном дереве поиска, в данном случае большую роль для поиска играет его свойство расположения
элементов (в правом поддереве больше и равно центральной вершины, в левом меньше и далее рекурсивно по дереву)
А чтобы удаление после себя правильное бинарное дерево необходимо следовать другому правилу: на место удаленного
элемента мы выбираем вершину самую правую в левом поддереве или самую левую в правом поддереве.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Удаления узла из бинарного дерева  - О(logh), где h - высота дерева

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Пространственная сложность - О(logh), выделение дополнительной памяти на стек вызовов рекурсии.

-- ID успешной посылки --
https://contest.yandex.ru/contest/24810/run-report/117881815/

"""

from typing import Optional


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def remove(root, key) -> Optional[Node]:
    if root is None:
        return None

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            min_right_node = find_min_right_node(root.right)
            root.value = min_right_node.value
            root.right = remove(root.right, min_right_node.value)
    return root


def find_min_right_node(node):
    while node.left is not None:
        node = node.left
    return node


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node8 = Node(None, None, 12)
    node6 = Node(node5, node8, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()