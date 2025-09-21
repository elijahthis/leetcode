class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ANALYSIS of Exponentation by Squaring
        # 1. If n is even, x^n = x^(n/2) * x^(n/2)
        # 2. If n is odd, x^n = x * x^(n/2) * x^(n/2)
        # 3. If n is negative, x^n = 1 / x^(-n)
        # 4. If n is 0, x^n = 1
        # 5. If x is 0, x^n = 0

        # Time complexity: O(log(n))
        # Space complexity: O(log(n))
        
        res = 1.0
        abs_n = abs(n)

        if x == 0:
            return 0

        if n == 0:
            return 1.0

        # to optimize, split even powers in two, and use  multiplication 
        if abs_n % 2 == 0:
            temp = self.myPow(x, abs_n/2)
            res = temp * temp
        else:
            temp = self.myPow(x, (abs_n-1)/2)
            res = x * temp * temp
       
        return res if n >=0 else 1 / res

        