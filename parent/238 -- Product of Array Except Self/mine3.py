class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time:  O(n). Two-pass
        # Space: O(1) extra space.
        # meets Leetcode's no-division constraint
        # same as mine2, but uses 1 array instead of 2

        n = len(nums)
        suff = nums[::] # output array
        pref_sum = 1
        suff[-1] = 1

        for i in range(1,n):
            suff[n-i-1] = nums[n-i] * suff[n-i]
        for i in range(1, n):
            pref_sum *= nums[i-1]
            suff[i] *= pref_sum
        
        return suff