class Solution:
    def canJump(self, nums):
        # Greedy Solution
        # Time: O(n)
        # Space: O(1)
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False

            furthest = max(furthest, i + nums[i])

        return True