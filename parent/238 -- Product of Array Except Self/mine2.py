class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time:  O(n). Two-pass
        # Space: O(n) extra space. Actually O(2n)
        # meets Leetcode's no-division constraint
        
        n = len(nums)
        res = [0] * n
        pref, suff = res[::], res[::]
        pref[0] = suff[-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
            suff[n-i-1] = nums[n-i] * suff[n-i]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res