class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        n = len(nums)
        hashSet = set(nums)
        total = nums[0]
        
        while i < n and nums[i] == nums[i-1]+1:
            total += nums[i]
            i += 1
        
        while total in hashSet:
            total += 1
        
        return total
