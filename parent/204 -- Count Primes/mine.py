class Solution:
    def countPrimes(self, n: int) -> int:
        # My implementation of the Sieve of Eratosthenes
        # Time: O(n log n). logically correct, but Suboptimal
        if n < 2:
            return 0
        sieve = [True] * (n-2)
        res = n-2
        idx = 0

        for idx in range(n-2):
            if sieve[idx]:
                prime, i = idx+2, 2
                while prime*i < n:
                    if sieve[prime*i-2]:
                        sieve[prime*i-2] = False
                        res -= 1
                    i += 1
        
        return res
