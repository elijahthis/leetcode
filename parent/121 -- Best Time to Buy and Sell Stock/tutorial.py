class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ANALYSIS:
        # - We can use two pointers to keep track of the current buy and sell prices
        # - We can use a variable to keep track of the max profit
        # - We can iterate through the prices and update the pointers and the max profit accordingly
        # - If the current price is less than the buy price, we update the buy price
        # - Otherwise, we update the max profit if the difference between the current price and the buy price is greater than the max profit
        # - We return the max profit
        # - Time complexity: O(n)
        # - Space complexity: O(1)
        left_ptr = 0
        right_ptr = 1
        max_profit = 0

        while right_ptr < len(prices):
            if prices[right_ptr] < prices[left_ptr]:
                left_ptr = right_ptr
            else:
                max_profit = max(max_profit, prices[right_ptr] - prices[left_ptr])
            right_ptr += 1
        
        return max_profit