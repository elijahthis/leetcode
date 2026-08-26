class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 1D DP with a sliding state
        rows, cols = len(matrix),  len(matrix[0])
        res = 0
        dp = matrix[-1]
        right = '0'

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows-1 or c == cols-1:
                    if matrix[r][c] == "1" and res == 0:
                        res = max(res, 1)
                    if c == cols-1:
                        right = matrix[r][c]
                    continue
                if matrix[r][c] != "0":
                    currVal = min(int(dp[c]), int(right), int(dp[c+1])) + 1
                    res = max(res, currVal)
                    dp[c+1] = right
                    if c == 0:
                        dp[c] = str(currVal)
                    else:
                        right = str(currVal)
                else:
                    dp[c+1] = right
                    if c == 0:
                        dp[c] = "0"
                    else:
                        right = "0"
        
        return res*res