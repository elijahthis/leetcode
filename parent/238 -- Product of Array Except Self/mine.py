class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time:  O(n). Two-pass
        # Space: O(1) extra space
        # interesting edge case of 1 r more zeros present
        # violates Leetcode's no-division constraint

        n = len(nums)
        prod, non_zero_prod, zero_count = 1, 1, 0
        for num in nums:
            prod *= num
            if num == 0:
                zero_count += 1
            else:
                non_zero_prod *= num
        res = [prod] * n
        
        if zero_count > 1:
            return res
        
        for i in range(n):
            if nums[i]:
                res[i] = int(res[i] / nums[i])
            else:
                res[i] = non_zero_prod
        
        return res