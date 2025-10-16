class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # Faster / Optimal

        res = 0
        i = 0

        while i < len(nums):
            while i < len(nums) and nums[i] != 1:
                i += 1
            
            curr = 0
            while i < len(nums) and nums[i] == 1:
                curr += 1
                i += 1
            res = max(res, curr)
        
        return res