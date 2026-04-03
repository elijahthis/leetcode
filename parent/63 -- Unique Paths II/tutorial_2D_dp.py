class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # Time: O(m × n)
        # Space: O(m × n)

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If start or end is blocked → no paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0  # obstacle blocks all paths
                else:
                    if r > 0:
                        dp[r][c] += dp[r - 1][c]
                    if c > 0:
                        dp[r][c] += dp[r][c - 1]

        return dp[m - 1][n - 1]
