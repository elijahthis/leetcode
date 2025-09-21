from typing import List

class Solution:
    #DYNAMIC PROGRAMMING
    # CORRECT SOLUTION
    # too much compliation
    def rob(self, nums: List[int]) -> int:
        max_val = 0
        dp = [0]*len(nums)

        for house in range(len(nums)):
            if house == 0:
                dp[house] = nums[0]
                max_val = nums[0]
            else:
                currMax = 0
                for item in dp[max(0, house-3):house-1]:
                    currMax = max(currMax, item)
                dp[house] = currMax + nums[house]
                max_val = max(max_val, dp[house])
        return max_val
    
        
soln = Solution()
print(soln.rob([2,1,1,2]))