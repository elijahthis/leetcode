import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ANALYSIS:
        # - binary search
        # - find the minimum k that satisfies the condition
        # - O(nlogm) time complexity, where n is the number of piles and m is the maximum number of bananas in a pile
        # - O(1) space complexity
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(float(p) / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
            