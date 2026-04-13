class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] represents the minimum number of coins needed to make amount i.
        # Initialize with infinity. Size is amount + 1 so dp[amount] is the answer.
        dp = [float("inf")] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                # If the coin is smaller than or equal to the current amount
                if i - c >= 0:
                    # The min coins for 'i' is either what we already found, 
                    # or 1 coin plus the min coins needed for the remainder (i - c)
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[amount] if dp[amount] != float("inf") else -1
        # return dp[-1] if dp[-1] != float("inf") else -1
                    