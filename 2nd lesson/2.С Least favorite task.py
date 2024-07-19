"""
C. Нелюбимое дело

Нужно написать только функцию, которая принимает на вход голову списка и номер удаляемого элемента и возвращает голову
обновлённого списка.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля). Список содержит не более

Формат вывода
Верните голову списка, в котором удален нужный элемент.
"""

import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    """delete random element"""
    while idx:
        node = node.next
        idx -= 1

    previous_node = get_node_by_index(head, index-1)

    new_node.next = previous_node.next
    previous_node.next = new_node

    previous_node =

    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()