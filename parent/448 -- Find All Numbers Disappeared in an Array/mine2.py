class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1). assuming res is not extra space
        # similar logic to leetcode #41
        # cyclic sort / index placement

        res = []

        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res