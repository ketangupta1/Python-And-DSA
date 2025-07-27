from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)
        s = self.q.qsize()
        for i in range(1,s):
            self.q.put(self.q.get())  # .get() will dequeu


    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        return self.q.queue[0]   # In python queue is designed to do put and get method peek is not thread safe that's why use deque for peek method.

    def empty(self) -> bool:
        return self.q.empty()