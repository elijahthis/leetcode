class Leaderboard:

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] = self.board.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # Time: O(NlogN+K)
        # Space: O(N)     --> Sorting creates a new list of size N
        return sum(sorted(self.board.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.board:
            del self.board[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


# Design a Leaderboard class, which has 3 functions:

# addScore(playerId, score): Update the leaderboard by adding score to the given player's score. 
# If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
# top(K): Return the score sum of the top K players.
# reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). 
# It is guaranteed that the player was added to the leaderboard before calling this function.
# Initially, the leaderboard is empty.