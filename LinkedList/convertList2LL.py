from dataclasses import dataclass
from typing import Optional

# @dataclass
# class Node:
#     data: int
#     next: Optional['Node'] = None  # Optional Node, default is None

class Node:
    def __init__(self, data, next:'Node' = None):
        self.data = data
        self.next = next

class ListToLinkedList:
    def __init__(self):
        self.head = None
    def ListToLL(self, lists) -> Node:
        self.head = Node(lists[0])
        mover = self.head
        for item in lists[1:]:
            temp = Node(item)
            mover.next = temp
            mover = temp
        return self.head

# LL = ListToLinkedList()
# head = LL.ListToLL([3,5,12,89])
# print(head.next.next.data)
