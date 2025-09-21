class Solution:
    def fib(self, n: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13, 21
        # recursive
        # Time Complexity: O(2^n)
        # Space Complexity: O(n)

        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)