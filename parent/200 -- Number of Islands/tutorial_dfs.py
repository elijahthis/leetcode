class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        # Not as effiient
        # passes leetcode, but could lead to recursion stak error in real-life large cases
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        result = 0
        
        def dfs(r,c):
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    dfs(nr, nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    result += 1
                    dfs(r,c)
        
        return result
