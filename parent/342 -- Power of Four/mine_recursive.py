class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Recursive Solution
        # Time complexity = O(log n)
        # Space complexity = O(log n)
        
        if n==4 or n == 1:
            return True
        elif n < 4:
            return False
        
        return self.isPowerOfFour(n/4)