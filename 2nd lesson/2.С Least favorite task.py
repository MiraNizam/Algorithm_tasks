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
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(node, idx):
    while idx: # это связный список и мы не можем обратить как к элементу массива по индексу, нам нужно дойти до нужного элемента
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
    previous_node.next_item = deleted_node.next_item
    print(node)


# def test():
node3 = Node("node3", None)
node2 = Node("node2", node3)
node1 = Node("node1", node2)
node0 = Node("node0", node1)
#     new_head =
solution(node0, 2)
#     assert new_head is node0
#     assert new_head.next_item is node2
#     assert new_head.next_item.next_item is node3
#     assert new_head.next_item.next_item.next_item is None
#     # result is node0 -> node2 -> node3
#
#
# if __name__ == '__main__':
#     test()