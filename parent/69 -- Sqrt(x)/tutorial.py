class Solution:
    def mySqrt(self, x: int) -> int:
        # Time: O(logn)
        # Binary search
        # fastest
        l,r = 0, x
        res = 0

        while l <= r:
            mid = (l+r)//2
            sqr = mid*mid
            if sqr > x:
                r = mid-1
            elif sqr < x:
                l = mid+1
                res = mid
            else:
                return mid
        
        return res