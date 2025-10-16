class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        
        count = 0
        total = 0

        for i in range(n):
            total += i+1
            count += 1

            if total >= n:
                return count if total == n else count-1
        