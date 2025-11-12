from collections import deque

def canReachOasis(grid, gas):
    m, n = len(grid), len(grid[0])
    start = dest = None

    # Find start and destination
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'c':
                start = (i, j)
            elif grid[i][j] == 'o':
                dest = (i, j)
    
    if not start or not dest:
        return False

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([(start[0], start[1], gas)])
    visited = set([(start[0], start[1], gas)])

    while queue:
        x, y, g = queue.popleft()
        if (x, y) == dest:
            return True
        if g == 0:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                new_gas = g - 1

                # If this cell is a gas station (integer)
                if isinstance(grid[nx][ny], int):
                    new_gas += grid[nx][ny]
                
                state = (nx, ny, new_gas)
                if new_gas >= 0 and state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, new_gas))

    return False


# grid = [
#     ['.', '.', '.', 'c', '.'],
#     ['.', '.', 2, '.', '.'],
#     ['.', '.', '.', '.', '.'],
#     ['.', '.', 'o', '.', '.']
# ]
# gas = 3

# print(canReachOasis(grid, gas))  # ✅ True (can refuel by +2 mid-way)