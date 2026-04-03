class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        nums.sort()
        for n in range(len(nums)):
            if nums[n] != n:
                return n
        return len(nums)