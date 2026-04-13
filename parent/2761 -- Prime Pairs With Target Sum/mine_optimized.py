class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # Goldbach pair finding problem.
        # builds on Sieve of Eratosthenes + a litle bit of 2Sum. love this one
        # Time: O(n log log n)
        # Space: O(n)
        
        if n < 3:
            return []
        sieve = [True]*n
        sieve[0] = sieve[1] = False
       
        res = []

        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n, i):
                    sieve[j] = False

        for i in range(2, n//2+1):
            if sieve[i] and sieve[n-i]:
                res.append([i, n-i])

        return res