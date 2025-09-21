class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Bitwise Solution: FASTEST
        # Time complexity = O(1)
        # Space complexity = O(1)

        return n > 0 and (n & (n - 1)) == 0