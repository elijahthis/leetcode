package main

func maximalSquare(matrix [][]byte) int {
	// Time: O(m*n)
	// Space: O(m*n)
	
	rows, cols := len(matrix), len(matrix[0])
	var res int

	dp := make([][]int, rows)
	for i := range dp {
		dp[i] = make([]int, cols)
	}
	for r := range rows {
		for c := range cols {
			dp[r][c] = int(matrix[r][c] - '0')
		}
	}

	for r := rows - 1; r >= 0; r-- {
		for c := cols - 1; c >= 0; c-- {
			if r == rows-1 || c == cols-1 {
				if dp[r][c] == 1 {
					res = max(res, 1)
				}
				continue
			}
			if dp[r][c] != 0 {
				down := dp[r+1][c]
				right := dp[r][c+1]
				downRight := dp[r+1][c+1]

				newVal := min(down, right, downRight) + 1

				res = max(res, newVal)
				dp[r][c] = newVal
			}
		}
	}

	return res * res
}
