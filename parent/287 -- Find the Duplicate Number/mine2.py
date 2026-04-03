class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 2 pointer. Floyd's Cycle Detection Algo
        slow = fast = 0

        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        
        return fast