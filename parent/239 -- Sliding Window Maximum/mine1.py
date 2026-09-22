from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Time: O(Nk). Passes Python, TLE Go
        # Space: O(k)

        res, curr_max = [], float('-inf')
        counts = {}
        l = 0

        for r in range(len(nums)):
            counts[nums[r]] = counts.get(nums[r], 0) + 1
            if r-l+1 < k:
                curr_max = max(curr_max, nums[r])
                continue

            if nums[r] >= curr_max:
                curr_max = nums[r]
            elif curr_max not in counts:
                curr_max = max(counts.keys())   # potential bottleneck. still passes tho
            
            res.append(curr_max)
            
            counts[nums[l]] -= 1
            if counts[nums[l]] == 0:
                del counts[nums[l]]
            l += 1
            
        return res
