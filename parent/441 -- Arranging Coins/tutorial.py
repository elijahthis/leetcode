import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Binary Search
        # Time: O(logn)
        # Space: O(1)
        # This is equivalent to finding the largest k such that:
            # (1 + 2 + 3 +...+ k) ≤ n
        # Sum of first k natural numbers: k*(k+1)/2.
        # So we want the largest k satisfying k*(k+1)/2≤n.
        # Binary search is perfect for this.
        
        l, r = 1, n

        while l <= r:
            k = (l + r) // 2
            coins_needed = (k*(k+1)) / 2
            if coins_needed == n:
                return k
            elif coins_needed < n:
                l = k+1
            else:
                r = k-1
        return r