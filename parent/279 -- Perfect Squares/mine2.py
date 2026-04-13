import math

class Solution:
    def numSquares(self, n: int) -> int:
        # modified to subtract squares. passed
        # this problem builds on rod-cutting
        squares = []
        res = [0]*n

        for i in range(1, math.floor(n**0.5)+1):
            res[(i*i)-1] = 1
            squares.append(i*i)
        

        def dfs(k):
            if res[k-1]:
                return res[k-1]

            minVal = float("inf")
            for s in squares:
                if s < k:
                    # minVal = min(minVal, dfs(s) + dfs(k-s))
                    minVal = min(minVal, dfs(k-s) + 1) # slightly more optimal
            
            res[k-1] = minVal
            return minVal
        
        dfs(n)
        return res[-1]