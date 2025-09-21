class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Recursive Solution
        # Time complexity = O(log n)
        # Space complexity = O(log n)

        if n < 1:
            return False
        elif n == 1 or n == 2:
            return True
        else:
            return self.isPowerOfTwo(n/2)