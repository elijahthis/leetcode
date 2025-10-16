class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # fastest. Two-pointer solution 
        
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        
        return l+1