class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time: O(m × n)
        # Space: O(m × n)
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dfs(r, c):
            # base case: bottom right
            if r == rows-1 and c == cols - 1:
                return grid[-1][-1]
            
            # check memo to avoid repeated work
            if (r,c) in memo:
                return memo[(r,c)]
            
            # Explore right and down paths
            right = dfs(r+1, c) if r < rows-1 else float('inf')
            down = dfs(r, c+1) if c < cols-1 else float('inf')

            # store in memo
            memo[(r,c)] = grid[r][c] + min(right, down)
            return memo[(r,c)]

        return dfs(0,0)