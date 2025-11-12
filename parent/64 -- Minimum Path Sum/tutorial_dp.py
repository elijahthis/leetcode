class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time: O(m × n)
        # Space: O(1) (in-place update)

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r][c-1], grid[r-1][c])
        
        return grid[-1][-1]