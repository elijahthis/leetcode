package main

func searchMatrix(matrix [][]int, target int) bool {
	rows := len(matrix)
	r, c := 0, len(matrix[0])-1

	for r < rows && c >= 0 {
		if matrix[r][c] == target {
			return true
		} else if matrix[r][c] < target {
			r += 1
		} else {
			c -= 1
		}
	}

	return false
}
