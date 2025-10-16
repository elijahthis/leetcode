class Solution:
    def numTrees(self, n: int) -> int:
        # Fastest (with symmetry optimization)
        # Time: O(n^2)
        # Space: O(n)

        dp = {
            0: 1, 
            1: 1, 
            2: 2
        }
        
        def helper(n: int) -> int:
            res = 0

            if n in dp:
                return dp[n]

            for i in range(n//2):
                res += (helper(i) * helper(n-i-1))
        
            # symmetry optimization
            res *= 2
            if n%2 == 1:
                mid = n//2
                res += (helper(mid) * helper(n-mid-1))

            dp[n] = res
            return dp[n]
        
        return helper(n)
