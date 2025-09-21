class Solution:
    def rob(self, nums: List[int]) -> int:
        # DYNAMIC PROGRAMMING
        # CORRECT AND SIMPLE SOLUTION
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # dp[i] = max(dp[i−1], dp[i−2]+nums[i])

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # simple pick or skip pattern
        for house in range(2, len(nums)):
            dp[house] = max(dp[house-1], dp[house-2] + nums[house])
        
        return dp[-1]