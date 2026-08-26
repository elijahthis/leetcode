class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 2D Bottom-Up DP
        # Time: O(m*n)
        # Space: O(1)

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows-1 or c == cols-1:
                    if matrix[r][c] == "1":
                        res = max(res, 1)
                    continue
                if matrix[r][c] != "0":
                    newVal = min(int(matrix[r+1][c]), int(matrix[r][c+1]), int(matrix[r+1][c+1])) + 1
                    res = max(res, newVal)
                    matrix[r][c] = str(newVal)
        
        return res*res
