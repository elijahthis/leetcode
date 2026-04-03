class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # sum of indexes == sum of elements. Missing Piece is missing number
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res