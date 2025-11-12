class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Logic being that if an element is the majority element, 
        # it'll always occupy the middle spot when the array is sorted
        # Time: O(n log n)
        # Space: O(1)
        # faster
        nums.sort()
        return nums[len(nums) // 2]