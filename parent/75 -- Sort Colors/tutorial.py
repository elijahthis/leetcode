class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We used the Dutch National Flag algorithm (invented by Dijkstra)
        # Time: O(n)
        # Space: O(1)
        lo, mid, hi = 0, 0, len(nums) - 1

        while mid <= hi:
            match nums[mid]:
                case 0:
                    nums[lo], nums[mid] = nums[mid], nums[lo]
                    lo += 1
                    mid += 1
                case 1:
                    mid += 1
                case _:
                    nums[mid], nums[hi] = nums[hi], nums[mid]
                    hi -= 1
