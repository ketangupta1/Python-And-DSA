'''Method 1: Here push is costly as O(N) but pop and peek is O(1) '''
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while (self.s1):
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while (self.s2):
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        if self.s1:
            return False
        return True

'''Method 2: Here push is O(1) but pop and peek is ocassionally O(N) '''


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:  # if s2 is not empty
            return self.s2.pop()
        else:
            while (self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        while (self.s1):
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        return False
