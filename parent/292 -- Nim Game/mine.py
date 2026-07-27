class Solution:
    def canWinNim(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return n % 4 != 0