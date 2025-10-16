class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1: 1, 2: 2}

        def dfs(n):
            if n in dp:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2)
            return dp[n]
        
        return dfs(n)