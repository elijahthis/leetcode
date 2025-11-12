import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Pure BFS
        # Time: O(n²) — each cell is visited once at most.
        # Space: O(n²) — for the queue and visited set.
         
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        directions = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1, -1], [-1,1]]

        visited = set([(0,0)])
        q = collections.deque([(0,0,1)])

        while q:
            r, c, steps = q.popleft()

            if r == n-1 and c == n-1:
                return steps

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr in range(n) and nc in range(n) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    q.append((nr, nc, steps+1))
                    visited.add((nr, nc))
            
        return -1