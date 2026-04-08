import heapq
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Time: O(n log k)
        # Space: O(n+k)
        
        k = len(primes)
        dp = [1] * n
        
        # heap entries: (value, prime_index, dp_index)
        heap = [(primes[i], i, 0) for i in range(k)]
        heapq.heapify(heap)

        for i in range(1, n):
            dp[i] = heap[0][0]

            # handle duplicates
            while heap and heap[0][0] == dp[i]:
                val, prime_idx, dp_idx = heapq.heappop(heap)
                new_val = primes[prime_idx] * dp[dp_idx + 1]
                heapq.heappush(heap, (new_val, prime_idx, dp_idx + 1))

        return dp[-1]