import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Best / Most optimal
        # DP with pointers
        # Each prime tracks which dp index it should multiply
        # Always pick the smallest candidate

        dp = [1]*n
        k = len(primes)
        next_multiples = primes[::]
        idx = [0]*k
        
        for i in range(1,n):
            dp[i] = min(next_multiples)

            for j in range(k):
                if dp[i] == next_multiples[j]:
                    idx[j] += 1
                    next_multiples[j] = dp[idx[j]]*primes[j]
            
        return dp[-1]