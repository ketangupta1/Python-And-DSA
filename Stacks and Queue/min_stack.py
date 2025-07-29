class MinStack:

    def __init__(self):
        self.st = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.min = val
        else:
            if self.min > val:
                new_val = 2 * val - self.min
                self.st.append(new_val)
                self.min = val
            else:
                self.st.append(val)

    def pop(self) -> None:
        if self.st[-1] < self.min:
            x = self.st.pop()
            new_min = 2 * self.min - x
            self.min = new_min
        else:
            self.st.pop()

    def top(self) -> int:
        if self.st[-1] < self.min:
            return self.min
        else:
            return self.st[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()