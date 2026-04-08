import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Passes, but uses far too much time/space. Need to optimize
        # Time: O(n * k * log(nk))
        # Space: O(nk)
        
        heap = []
        dp = [1]*n
        visit = set()
        
        for i in range(1,n):
            for p in primes:
                val = dp[i-1]*p
                if val not in visit:
                    heapq.heappush(heap, val)
                    visit.add(val)
            
            dp[i] = heapq.heappop(heap)
        return dp[-1]
                