class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(M×N)
        # Space: O(M×N)
        # Higher overhead

        res = []
        visited = set()
        M, N = len(matrix), len(matrix[0])
        hashM = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}

        def outOfBounds(r, c):
            return (not (0 <= r < M)) or (not (0 <= c < N)) or (r, c) in visited

        def dfs(r, c, h, v):
            if outOfBounds(r, c):
                return

            res.append(matrix[r][c])
            visited.add((r, c))

            if outOfBounds(r + v, c + h):
                nh, nv = hashM[(h, v)]
                dfs(r + nv, c + nh, nh, nv)
            else:
                dfs(r + v, c + h, h, v)

        dfs(0, 0, 1, 0)
        return res