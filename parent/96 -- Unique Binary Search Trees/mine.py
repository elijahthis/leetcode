class Solution:
    def numTrees(self, n: int) -> int:
        if not n:
            return 1
        if n < 3:
            return n
        
        dp = {
            0: 1, 
            1: 1, 
            2: 2
        }
        res = 0
        if n in dp:
            return dp[n]


        for i in range(n//2):
            res += (self.numTrees(i) * self.numTrees(n-i-1))
        
        # symmetry optimization
        res *= 2
        if n%2 == 1:
            mid = n//2
            res += (self.numTrees(mid) * self.numTrees(n-mid-1))
        
        return res
