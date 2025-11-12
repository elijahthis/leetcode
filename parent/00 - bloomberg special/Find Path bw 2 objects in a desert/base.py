from collections import deque

def canReachOasis(grid, gas):
    # Breadth-First Search (BFS) with obstacle check
    # obstacle = #
    
    m, n = len(grid), len(grid[0])
    start = None
    dest = None

    # Find car and oasis
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'c':
                start = (i, j)
            elif grid[i][j] == 'o':
                dest = (i, j)

    if not start or not dest:
        return False

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], gas)])
    visited = set([start])

    while queue:
        x, y, g = queue.popleft()
        if (x, y) == dest:
            return True
        if g == 0:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, g - 1))

    return False
