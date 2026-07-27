class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Solution (there's a DP one?)
        # Time: O(n)
        # Space: O(1)
        lastInd = 0
        for i in range(len(nums)):
            lastInd = max(lastInd, nums[i]+i)
            if nums[i] == 0 and lastInd <= i:
                break
            # early return
            # if lastInd >= len(nums)-1:
            #     return True
        
        return lastInd >= len(nums)-1