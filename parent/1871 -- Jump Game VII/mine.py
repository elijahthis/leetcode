class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # DP + Prefix sum sliding window
        # Time: O(n)
        # Space: O(n)

        n = len(s)
        
        dp = [0] * n
        canReach = 0

        if s[-1] == "0":
            dp[0] = 1
        
        for i in range(1, n):
            if i >= minJump:
                canReach += dp[i - minJump]
            if i > maxJump:
                canReach -= dp[i - maxJump - 1]
            
            real_ind = n-i-1
            if i >= minJump and s[real_ind] == "0" and canReach > 0:
                dp[i] = 1
                
        return dp[-1] == 1