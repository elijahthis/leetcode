class BrowserHistory:

    def __init__(self, homepage: str):
        self.historyStack = [homepage]
        self.ptr = 0
        self.last = 0   # tracks the end of valid history

    def visit(self, url: str) -> None:
        self.ptr += 1
        
        if self.ptr == len(self.historyStack):
            self.historyStack.append(url)
        else:
            self.historyStack[self.ptr] = url
        
        self.last = self.ptr   # truncate forward history logically

    def back(self, steps: int) -> str:
        self.ptr = max(0, self.ptr - steps)
        return self.historyStack[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr = min(self.last, self.ptr + steps)
        return self.historyStack[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)