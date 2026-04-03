class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time: O(m*n)
        # Space: O(n)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        # If start is blocked -> no paths
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c-1]
        
        return dp[-1]