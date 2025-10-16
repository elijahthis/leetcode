import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        log_val = math.log(n, 2)
        return abs(round(log_val) - log_val) < 1e-10