from dataclasses import dataclass
from typing import Optional


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
        print()

    def deleteHead(self) -> Node:
        if not self.head:  # Always check this null condition(Edge Case)
            return self.head
        self.head = self.head.next
        return self.head
    
    def deleteTail(self):
        if not self.head or self.head.next is None:  # Check for if there is only one element in LL
            return None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return self.head
    
    def deleteKthNode(self, k) -> Node:
        if not self.head:
            return None
        if k == 1:
            self.head = self.head.next
            return self.head
        count = 1
        temp = self.head
        prev = None
        while temp:
            if count == k:
                prev.next = prev.next.next
                break
            prev = temp
            temp = temp.next
            count += 1
        return self.head

        



ll = ListToLinkedList()
head = ll.ListToLL([3,5,12,89,123,78])
ll.traverseAndPrint(head)
head = ll.deleteHead()
ll.traverseAndPrint(head)
head = ll.deleteTail()
ll.traverseAndPrint(head)
head = ll.deleteKthNode(3)
ll.traverseAndPrint(head)
# print(head.next.next.data)
