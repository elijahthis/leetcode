class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # first try. sorted gap detection
        # Time: O(n log n). Unfortunately does not meet the O(n) time requirement
        # Space: O(n log n). Unfortunately does not meet the O(1) aux space requirement
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            i += 1
        if i == len(nums) or nums[i] != 1:
            return 1
        
        for j in range(i+1, len(nums)):
            if nums[j] > nums[j-1]+1:
                return nums[j-1]+1
        
        return nums[-1]+1