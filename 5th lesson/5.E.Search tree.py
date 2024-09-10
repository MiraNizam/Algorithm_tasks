"""
E. Дерево поиска
написать функцию, которая определяет, является ли заданное дерево деревом поиска. Значения в левом поддереве должны
быть строго меньше, в правом —- строго больше значения в узле.

Формат ввода
На вход функции подается корень бинарного дерева.

Формат вывода
Функция должна вернуть True, если дерево является деревом поиска, иначе - False.

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root, min_value=float("-inf"), max_value=float("inf")):
    if root is None:
        return True

    if not (min_value < root.value < max_value):
        return False

    left_subtree = solution(root.left, min_value, root.value)
    right_subtree = solution(root.right, root.value, max_value)
    return left_subtree and right_subtree


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()