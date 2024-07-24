"""
C. Нелюбимое дело

Нужно написать только функцию, которая принимает на вход голову списка и номер удаляемого элемента и возвращает голову
обновлённого списка.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля). Список содержит не более

Формат вывода
Верните голову списка, в котором удален нужный элемент.
"""


class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def get_node_by_index(node, idx):
    while idx:
        node = node.next_item
        idx -= 1
    return node


def solution(node, idx):
    if idx == 0:
        node = node.next_item
        return node

    previous_node = get_node_by_index(node, idx-1)
    deleted_node = get_node_by_index(node, idx)
    if deleted_node.next_item is None:
        previous_node.next_item = None
    else:
        previous_node.next_item = deleted_node.next_item
    return node


node6 = Node("node6", None)
node5 = Node("node5", node6)
node4 = Node("node4", node5)
node3 = Node("node3", node4)
node2 = Node("node2", node3)
node1 = Node("node1", node2)
node0 = Node("node0", node1)

print(solution(node0, 4))