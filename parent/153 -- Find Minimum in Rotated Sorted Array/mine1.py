class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search
        # Time: O(logn)
        # Space: O(1)

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] >= nums[l]:
                return nums[l]
            elif nums[mid] < nums[r]:
                r = mid
            