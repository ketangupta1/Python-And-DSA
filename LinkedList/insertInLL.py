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

    def insertAtHead(self, data) -> Node:
        # self.data = data     # Bcz Adds self.data, which is irrelevant to the class as a whole
        self.head = Node(data, self.head)
        return self.head
    
    def insertAtLast(self, data) -> Node:
        if self.head is None:
            self.head = Node(data)
            return self.head
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = Node(data)
                break
            temp = temp.next
        return self.head
    
    def insertAtKth(self, k, data):
        if self.head is None or k == 1:
            return Node(data)
        temp = self.head
        prev = None
        count = 1
        while temp:
            if count == k:
                temp = Node(data, temp)
                prev.next = temp
                break
            prev = temp
            temp = temp.next
            count += 1
        return self.head
            
        



ll = ListToLinkedList()
head = ll.ListToLL([3,5,12])
ll.traverseAndPrint(head)
head = ll.insertAtHead(89)
ll.traverseAndPrint(head)
head = ll.insertAtLast(25)
ll.traverseAndPrint(head)
head = ll.insertAtKth(3,67)
ll.traverseAndPrint(head)
