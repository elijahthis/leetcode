class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # most interviews don't want you to sort
        nums.sort()
        return nums[-1*k]