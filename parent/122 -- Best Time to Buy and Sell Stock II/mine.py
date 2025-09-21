class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ANALYSIS:
        # - We can use a variable to keep track of the max profit
        # - We can iterate through the prices and update the max profit accordingly
        # - If the difference between the current price and the next price is greater than 0, we add it to the max profit
        # - We return the max profit
        # - Time complexity: O(n)
        # - Space complexity: O(1)
        max_p = 0

        for i, price in enumerate(prices):
            if i < len(prices) - 1:
                diff = prices[i+1] - price
                if diff > 0:
                    max_p += diff
        
        return max_p