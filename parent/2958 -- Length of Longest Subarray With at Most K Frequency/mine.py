class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Sliding Window
        # Time: O(n)
        # Space: O(n)
        res = 1
        counts = {nums[0]: 1}
        l,r = 0, 1
        
        while l <= r and r < len(nums):
            counts[nums[r]] = counts.get(nums[r], 0) + 1
            while l <= r and counts[nums[r]] > k:
                counts[nums[l]] -= 1
                l +=1

            res = max(res, r-l+1)
            r += 1

        return res