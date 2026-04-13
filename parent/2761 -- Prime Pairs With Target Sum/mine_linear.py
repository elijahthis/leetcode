class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n < 3:
            return []
        
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        primes = []

        # Linear sieve
        for i in range(2, n):
            if sieve[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:
                    break
                sieve[i * p] = False
                if i % p == 0:
                    break

        # Find pairs
        res = []
        for i in range(2, n // 2 + 1):
            if sieve[i] and sieve[n - i]:
                res.append([i, n - i])
        
        return res