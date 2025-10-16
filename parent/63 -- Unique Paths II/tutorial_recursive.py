class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Time: O(M × N)
        # Space: O(M × N)

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(M-1,N-1): 1}

        def dfs(r, c):
            # base case
            # out of bounds or cell contains 1 (obstacle)
            if r == M or c == N or obstacleGrid[r][c]:
                return 0
            # avoid repeated work
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return dp[(r,c)]
        
        return dfs(0,0)