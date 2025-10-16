class Solution:
    def mySqrt(self, x: int) -> int:
        # Time: O(√n)
        if x < 2:
            return x
        for i in range(x+1):
            sqr = i*i
            if sqr >= x:
                return i if sqr == x else i-1