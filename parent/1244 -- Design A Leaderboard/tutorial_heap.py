import heapq
class Leaderboard:

    def __init__(self):
        self.board = {}  #id -> score O(1)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] = self.board.get(playerId, 0) + score
        

    def top(self, K: int) -> int:
        # heap is faster: O(nlogk)
        
        # return sum(heapq.nlargest(K, self.board.values))
        # manually
        heap = []
        for score in self.board.values():
            heapq.heappush(heap, score)
            if len(heap) > K:
                heapq.heappop(heap)
        
        return sum(heap)

    def reset(self, playerId: int) -> None:
        if playerId in self.board:
            del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)