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

# dll = doublyLL()
# head = dll.arryToDLL([2,4,8,1,10,89,43])
# dll.traverseDLL()
