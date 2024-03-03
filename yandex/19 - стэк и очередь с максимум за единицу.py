
class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def insert(self, val):
        self.stack.append(val)
        if self.max_stack:
            self.max_stack.append(max(val, self.max_stack[-1]))
        else:
            self.stack.append(val)

    def pop(self) -> int:
        val = self.stack.pop()
        self.max_stack.pop()
        return val

    def max(self) -> int:
        return self.max_stack[-1]



from collections import deque

class QueueMax:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()

    def insert(self, val) -> None:
        """O(N)"""
        self.queue.append(val)
        self.max_queue.append(self.max_queue[-1])
        for i in range(len(self.max_queue)-1, -1, -1):
            if self.max_queue[i] < val:
                self.max_queue[i] = val
            else:
                break

    def pop(self) -> int:
        """O(1)"""
        val = self.queue.popleft()
        self.max_queue.popleft()
        return val

    def max(self) -> int:
        """O(1)"""
        return self.max_queue[0]
