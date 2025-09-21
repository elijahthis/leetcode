class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # iterative solution
        # Time complexity = O(log n)
        # Space complexity = O(1) (eliminates recursion)
        
        if n < 1:
            return False
        
        while n%3 == 0:
            n //= 3

        return n == 1