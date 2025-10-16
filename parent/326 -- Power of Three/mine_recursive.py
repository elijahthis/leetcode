class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Recursive Solution
        # Time complexity = O(log n)
        # Space complexity = O(log n)
        
        if n == 1:
            return True
        elif n < 1 or n%3 != 0:
            return False
        
        return self.isPowerOfThree(n/3)