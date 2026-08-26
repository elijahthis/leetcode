class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        # Only keep track of the row below the current one
        dp = [0] * (cols + 1)
        
        for r in range(rows - 1, -1, -1):
            next_dp = [0] * (cols + 1)
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == "1":
                    # DP state depends on right, down, and diagonal-down-right
                    next_dp[c] = min(next_dp[c+1], dp[c], dp[c+1]) + 1
                    res = max(res, next_dp[c])
            dp = next_dp
            
        return res * res