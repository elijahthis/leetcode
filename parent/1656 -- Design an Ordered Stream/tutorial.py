class OrderedStream:
    # ANALYSIS:
    # - We are given a stream of n elements
    # - We are given a function insert(idKey, value) that inserts a value at the idKey index
    # - We are to return a list of values that are contiguous from the start of the stream
    # - We are to return the list of values in the order they were inserted

    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        # We are given the idKey index and the value to insert
        # We insert the value at the idKey index
        # We return a list of contiguous values from the start of the stream
        self.stream[idKey - 1] = value
        result = []

        while self.ptr < len(self.stream) and self.stream[self.ptr] != None:
            result.append(self.stream[self.ptr])
            self.ptr += 1
        
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)