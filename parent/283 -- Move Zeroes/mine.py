class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        diff = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                diff += 1
            else:
                nums[i-diff] = nums[i]
        for i in range(diff):
            nums[len(nums)-i-1] = 0