from typing import List

class Solution:
    """ CORRECT, but not optimal
        Passes all test cases
    """
    def countBits(self, n: int) -> List[int]:
        dp_count = [0] * (n+1)

        def convertAndCount(n):
            if dp_count[i]:
                return dp_count[i]
            else:
                res = 0
                if n == 0 or n == 1:
                    res += n
                else:
                    val = n // 2
                    rem = n % 2

                    res += rem
                        
                    if val > 0:
                        res += convertAndCount(val) 

                return res

        for i in range(n+1):
            dp_count[i] = convertAndCount(i) 

        return dp_count

    
    