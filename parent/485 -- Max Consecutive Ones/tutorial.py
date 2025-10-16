class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # Clearer / Easier to explain
        res = count = 0

        for n in nums:
            if n == 1:
                count += 1
                res = max(count, res)
            else:
                count = 0
        
        return res