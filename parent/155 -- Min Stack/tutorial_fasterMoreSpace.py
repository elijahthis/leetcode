class MinStack:
    # follow-up: Why do we need two stacks? Can we do it with one?
    # yes, you can do it with one stack if each element stores both value and currentMin

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append([val, minVal])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()