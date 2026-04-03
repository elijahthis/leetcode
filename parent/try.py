from collections import deque
def canReachOasis(grid, gas):
    """
    [
        ["c",".","."]
        [".",".","."]
        [".","o","."]
    ]
    """
    rows, cols = len(grid), len(grid[0])
    start = dest = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "c":
                start = (r,c)
            elif grid[r][c] == "o":
                dest = (r,c)

    q = deque([start[0], start[1], gas])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        r,c,g = q.popleft()

        if (r,c) == dest:
            return True

        if g == 0:
            continue
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != "#":
                new_gas = g - 1
                if isinstance(grid[nr][nc], int):
                    new_gas += grid[nr][nc]

                visited.add((nr,nc))
                q.append((nr, nc, new_gas))
    
    return False



