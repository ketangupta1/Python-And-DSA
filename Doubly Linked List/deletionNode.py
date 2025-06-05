class Node:
    def __init__(self, data, next:'Node'=None, back:'Node'=None):
        self.data = data
        self.next = next
        self.back = back

class doublyLL:
    def __init__(self):
        self.head = None

    def arryToDLL(self, arr):
        self.head = Node(arr[0])
        prev = self.head
        for item in arr[1:]:
            temp = Node(item, None, prev)
            prev.next = temp
            prev = temp
        return self.head

    def traverseDLL(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end = " ")
            temp = temp.next
        print()

    def deleteHead(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        prev = self.head
        self.head = self.head.next
        self.head.back = None
        prev.next = None
        return
    
    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        temp = self.head
        while temp:
            if temp.next is None:
                temp.back.next = None
                temp.back = None
            temp = temp.next
        return None
    
    def deleteKthNode(self, k):
        if self.head is None:
            return None
        temp = self.head
        count = 1
        while temp:
            if count == k:
                break
            temp = temp.next
            count += 1
        prev = temp.back
        front = temp.next
        if prev is None and front is None:
            temp = None
        elif prev is None:
            self.deleteHead()
        elif front is None:
            self.deleteLast()
        else:
            prev.next = front
            front.back = prev
            temp.back = None
            temp.next = None
        return
        

dll = doublyLL()
head = dll.arryToDLL([2,4,8,1,10,89,43])
dll.traverseDLL()
dll.deleteHead()
dll.traverseDLL()
dll.deleteLast()
dll.traverseDLL()
dll.deleteKthNode(3)
dll.traverseDLL()
