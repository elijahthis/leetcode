class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Iterative Solution
        # Time complexity = O(log n)
        # Space complexity = O(1) (eliminates recursion)

        if n < 1:
            return False
        
        while n % 2 == 0:
            n //= 2
        
        return n == 1