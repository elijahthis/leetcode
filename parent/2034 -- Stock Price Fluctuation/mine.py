import heapq

class StockPrice:
    # two heaps (max and min) tokeep track of max and min price
    # prices hashmap to store correct price and ttrack stale prices

    def __init__(self):
        # Space: O(n)
        self.prices = {}        # {timestamp -> price}
        self.minHeap = []       # (price, timestamp)
        self.maxHeap = []       # (price, timestamp)
        self.last_updated = float('-inf')

    def update(self, timestamp: int, price: int) -> None:
        # Time: O(log n)
        heapq.heappush(self.minHeap, (price, timestamp))
        heapq.heappush(self.maxHeap, (price*-1, timestamp*-1))
        self.prices[timestamp] = price
        self.last_updated = max(self.last_updated, timestamp)
    
    def current(self) -> int:
        # Time: O(1)
        return self.prices[self.last_updated]

    def maximum(self) -> int:
        # Time: O(log n)
        while self.maxHeap[0][0]*-1 != self.prices[self.maxHeap[0][1]*-1]:
            heapq.heappop(self.maxHeap)
        return self.maxHeap[0][0] * -1

    def minimum(self) -> int:
        # Time: O(log n)
        while self.minHeap[0][0] != self.prices[self.minHeap[0][1]]:
            heapq.heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()