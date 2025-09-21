class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                max_p += profit
                
        return max_p