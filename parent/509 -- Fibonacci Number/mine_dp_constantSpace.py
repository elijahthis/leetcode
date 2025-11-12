class Solution:
    def fib(self, n: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13, 21
        # Dynamic Programming
        if n < 2:
            return n
        
        fib1, fib2 = 0, 1
        
        for _ in range(2, n+1):
            fib1, fib2 = fib2, fib1+fib2
        
        return fib2