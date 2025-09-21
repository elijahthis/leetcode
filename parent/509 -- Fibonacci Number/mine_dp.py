class Solution:
    def fib(self, n: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13, 21
        # Dynamic Programming
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        if n == 0:
            return n

        dp = [0] * (n+1)
        dp[1] = 1
        
        for ind in range(2, n+1):
            dp[ind] = dp[ind-1] + dp[ind-2]
        
        return dp[n]