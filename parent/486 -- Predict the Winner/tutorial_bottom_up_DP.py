class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Bottom-Up DP approach (2D)
        # Time: O(n^2)
        # Space: O(n^2)

        n = len(nums)
        
        # dp[i][j] stores the maximum score DIFFERENCE the current 
        # player can achieve over the opponent using the subarray nums[i...j]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: When the subarray is length 1 (i == j), 
        # the current player just takes that single number.
        for i in range(n):
            dp[i][i] = nums[i]
            
        # Build the DP table for subarrays of length 2 up to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # The current player chooses either the left or right element.
                # They gain that element's value, but lose the score difference 
                # the opponent will achieve in the remaining subarray.
                take_left = nums[i] - dp[i + 1][j]
                take_right = nums[j] - dp[i][j - 1]
                
                dp[i][j] = max(take_left, take_right)
                
        # If the score difference for the entire array is >= 0, Player 1 wins
        return dp[0][n - 1] >= 0