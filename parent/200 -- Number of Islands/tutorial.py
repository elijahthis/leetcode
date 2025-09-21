import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ANALYSIS:
        # - We can use a BFS to traverse the grid
        # - We can iterate through the grid and when we encounter a 1, we can increment the number of islands
        # - We can then perform a BFS to traverse the island and mark the cells as visited
        # - We can then increment the number of islands


        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            # Perform a BFS
            # We keep track of the cells that have been visited
            # We add the cell to the queue and mark it as visited
            # We then iterate through the neighbors of the cell and add them to the queue if they are valid cells
            # We mark the neighbors
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    next_row = row+dr
                    next_col = col+dc
                    if ((next_row) in range(rows) and (next_col) in range(cols) and grid[next_row][next_col] == "1" and (next_row, next_col) not in visited):
                        q.append((next_row, next_col))
                        visited.add((next_row, next_col))
                


        # Iterate through the grid
        # If we encounter a 1 and the cell has not been visited, we perform a BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands