class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # Goldbach pair finding problem
        # builds on Sieve of Eratosthenes + a litle bit of 2Sum
        # Time: O(n log log n)
        # Space: O(n)

        if n < 3:
            return []
        sieve = [True]*n
        sieve[0] = sieve[1] = False
        primes = []
        res = []
        hashP = set()

        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n, i):
                    sieve[j] = False
        for i in range(2, n):
            if sieve[i]:
                primes.append(i)
        
        for p in primes:
            rem = n-p
            if rem in hashP or p+p == n:
                res.append([rem, p])
            hashP.add(p)

        return res[::-1]