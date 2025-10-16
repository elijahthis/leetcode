class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bitwise operation
        res = 0

        for n in nums:
            res = res ^ n

        return res