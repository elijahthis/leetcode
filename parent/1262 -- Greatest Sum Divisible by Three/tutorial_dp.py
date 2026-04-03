class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -10**15, -10**15]  # dp[r] = best sum with remainder r
        
        for x in nums:
            prev = dp[:]  # take snapshot
            for r in range(3):
                new_r = (r + x) % 3
                dp[new_r] = max(dp[new_r], prev[r] + x)
        
        return dp[0]

# [3,6,5,1,8],m 