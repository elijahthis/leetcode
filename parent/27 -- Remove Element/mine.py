class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        diff = 0
        for i in range(len(nums)):
            if nums[i] == val:
                diff += 1
            else:
                nums[i-diff] = nums[i]
        
        return len(nums) - diff