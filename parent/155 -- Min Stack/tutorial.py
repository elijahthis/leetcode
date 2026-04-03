class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Always push val onto stack.
        # For minStack, push the minimum between:
        # the new value val, and
        # the current minimum minStack[-1] (if it exists).
        # So at every point, minStack[i] = minimum of the first i+1 elements.
        self.stack.append(val)
        # minVal = self.minStack[-1] if self.minStack and self.minStack[-1] < val else val
        minVal = min(self.minStack[-1], val) if self.minStack else val
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()