class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom-Up DP (most efficient. improves Space)
        # Time: O(amount*n)
        # Space: O(amount)

        dp = [0] * (amount+1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount+1):
                if i >= 0:
                    dp[i] += dp[i-c]

        return dp[-1]
            