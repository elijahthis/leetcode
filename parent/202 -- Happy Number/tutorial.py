class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(d) where d = number of digits in n
        # Space: O(1). More precisely, O(k) where k = number of unique states before cycle, but k is bounded so treat as O(1)
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)

            total = 0
            while n:
                digit = n%10
                total += digit*digit
                n //= 10
            
            n = total
        
        return n == 1