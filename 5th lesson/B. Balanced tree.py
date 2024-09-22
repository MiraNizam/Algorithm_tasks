"""
B. Сбалансированное дерево

Функция, которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья каждой вершины отличаются по высоте не больше, чем на
единицу.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def height(node) -> int:
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def solution(root):
    if root is None:
        return True

    left_balanced = solution(root.left)
    right_balanced = solution(root.right)

    left_height = height(root.left)
    right_height = height(root.right)

    check_for_balance = left_balanced and right_balanced and abs(left_height - right_height) <= 1

    return check_for_balance


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()