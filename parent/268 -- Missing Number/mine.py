class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        set_nums = set(nums)
        for n in range(len(nums)+1):
            if n not in set_nums:
                return n