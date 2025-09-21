from typing import List

class Solution:
    # DYNAMIC PROGRAMMING
    # CORRECT AND SIMPLE SOLUTION
        # Time Complexity: O(n)
        # Space Complexity: O(1) -- Constant space
        # same pick or skip pattern
        # we can make it constant space because we only need the last two elements in our dp array to proceed
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)

        return rob2
    
        
soln = Solution()
print(soln.rob([2,1,1,2]))