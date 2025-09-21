class BrowserHistory:

    def __init__(self, homepage: str):
        self.historyStack = [homepage] # stack to keep track of the history
        self.ptr = 0     # pointer to keep track of the current page

    def visit(self, url: str) -> None:
        self.historyStack = self.historyStack[:self.ptr+1] + [url] # we only keep the history up to the current page
        self.ptr += 1 # we move the pointer to the current page

    def back(self, steps: int) -> str:
        # we move the pointer back by steps
        # we make sure the pointer does not go below 0
        self.ptr = max(self.ptr - steps, 0)
        return self.historyStack[self.ptr]

    def forward(self, steps: int) -> str:
        # we move the pointer forward by steps
        # we make sure the pointer does not go above the length of the history stack
        self.ptr = min(self.ptr + steps, len(self.historyStack)-1)
        return self.historyStack[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)