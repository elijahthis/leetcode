class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        return list(set(list(range(1,len(nums)+1)))-set(nums))