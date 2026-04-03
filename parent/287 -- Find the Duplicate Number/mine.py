class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Set approach
        # Time: O(n)
        # Space: O(n). Doesn't meet criteria of constant space
        visited = set()

        for n in nums:
            if n in visited:
                return n
            visited.add(n)