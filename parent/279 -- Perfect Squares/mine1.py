import math

class Solution:
    def numSquares(self, n: int) -> int:
        # my first dp try
        # correct, but TLE's at the high end. 7168, 7468,...
        # partition-based DP
        res = [0]*n
        for i in range(1, math.floor(n**0.5)+1):
            res[(i*i)-1] = 1
            

        def dfs(k):
            if res[k-1]:
                return res[k-1]

            minVal = float("inf")
            for i in range(k//2):
                minVal = min(minVal, dfs(i+1) + dfs(k-i-1))
            
            res[k-1] = minVal
            return minVal
        
        dfs(n)
        return res[-1]