class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        # curr alone (start fresh)
        # max_so_far * curr
        # min_so_far * curr (two negatives → positive)

        res = min_so_far = max_so_far = nums[0]
        
        for i in range(1, len(nums)):
            candidates = (nums[i], nums[i]*min_so_far, nums[i]*max_so_far)
            min_so_far = min(candidates)
            max_so_far = max(candidates)
            res = max(max_so_far, res)

        return res