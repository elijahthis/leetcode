class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        nums.sort()

        return max((nums[0]-1)*(nums[1]-1), (nums[-1]-1)*(nums[-2]-1))