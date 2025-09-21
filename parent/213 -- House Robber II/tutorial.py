from typing import List

class Solution:
    #DYNAMIC PROGRAMMING
    # Circular version of robber1
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def rob(self, nums: List[int]) -> int:
        # Break it into two linear problems and find the max:
        # nums[:-1] and nums[1:]
        # Basically run robber1 on everything but the first, everything but the last, and find the max
        # add nums[0] to the mix in case nums has just one item
        return max(nums[0], self.robLinear(nums[:-1]), self.robLinear(nums[1:]))
        
    def robLinear(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        for num in nums:
            rob1, rob2 = rob2, max(rob2, rob1+num)
        return rob2
    

   
        
soln = Solution()
print(soln.rob([2,1,1,2]))