class Solution:
    def jump(self, nums: list[int]) -> int:
        # Bottom-up DP
        # Time: O(n^2)
        # Space: O(n)
        
        n = len(nums)
        
        # Initialize DP array with infinity. 
        # dp[i] will store the min jumps to reach index i.
        dp = [float('inf')] * n
        dp[0] = 0  # 0 jumps needed to stand at the starting line
        
        for i in range(n):
            # From the current position i, update all reachable future positions
            for step in range(1, nums[i] + 1):
                if i + step < n:
                    # The min jumps to reach (i + step) is either its current known 
                    # min jumps, or the jumps to reach i plus 1 more jump.
                    dp[i + step] = min(dp[i + step], dp[i] + 1)
                    
        return dp[-1]