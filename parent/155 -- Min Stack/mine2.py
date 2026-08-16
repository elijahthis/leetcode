class MinStack:
    # slightly easier to think about
    # Still optimal
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)

    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()