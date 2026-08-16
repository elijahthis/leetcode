class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Time: O(n)
        # Space: O(1)
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        
        if prod % t == 0:
            return n
        
        last_digit = int(str(n)[-1])
        prod /= last_digit
        
        for i in range(last_digit+1, 10):
            prod *= i
            if prod % t == 0:
                return n + (i-int(str(n)[-1]))
            prod /= i
        
        return (n // 10 + 1) * 10