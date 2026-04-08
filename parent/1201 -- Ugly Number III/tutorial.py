import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # Time: O(logn)
        # Space: O(1)
        # Uses a bit of set theory and math
        # A, B, C - set of all +ve integers <= N, that are divisible by a,b,c
        # F(N) = A + B + C - (AnB) - (AnC) - (BnC) + (AnBnC). --> this is the function for our problem. total no. of elements in these sets, (removing duplicates)
        # We need to find the least integer N for which F(N) >= n

        l, r = min(a,b,c), max(a,b,c) * n
        res = 1

        while l < r:
            N = (l + r) // 2
            FN = (N // a) + (N // b) + (N // c) - (N // math.lcm(a,b)) - (N // math.lcm(a,c)) - (N // math.lcm(b,c)) + (N // math.lcm(a,b,c))

            if FN < n:
                l = N+1
            else:
                # where F(N) >= n
                r = N
        
        return l    # or r
        