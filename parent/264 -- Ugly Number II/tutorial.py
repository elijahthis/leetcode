import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 3 Pointer + 2D-DP solution
        dp = [1] * n
        p2 = p3 = p5 = 0

        for i in range(1,n):
            val2 = dp[p2]*2
            val3 = dp[p3]*3
            val5 = dp[p5]*5

            dp[i] = min(val2, val3, val5)

            if dp[i] == val2:
                p2 += 1
            if dp[i] == val3:
                p3 += 1
            if dp[i] == val5:
                p5 += 1
            
        
        return dp[-1]