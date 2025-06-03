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
    def traverseAndPrint(self, head):
        temp = head
        while temp:
            print(f"{temp.data}->", end=" ")
            temp = temp.next

# ll = ListToLinkedList()
# head = ll.ListToLL([3,5,12,89,123,78])
# ll.traverseAndPrint(head)
