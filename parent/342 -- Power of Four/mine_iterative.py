class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Iterative Solution
        # Time complexity = O(log n)
        # Space complexity = O(1) (eliminates recursion)
        
        if n < 1:
            return False
        
        while n%4 == 0:
            n //= 4

        return n == 1