class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        isIncr = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if isIncr == -1:
                    return False
                isIncr = 1
            elif nums[i] < nums[i-1]:
                if isIncr == 1:
                    return False
                isIncr = -1
        
        return True
            