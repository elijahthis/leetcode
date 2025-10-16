import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # math solution
        # k(k+1)/2 <= n -- formula for sum of first n numbers. solve for k

        # Time: O(1)
        # Space: O(1)

        return int((math.sqrt(8*n +1) -1)/2)
        