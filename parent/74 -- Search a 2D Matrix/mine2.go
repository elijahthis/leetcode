package main

func searchMatrix(matrix [][]int, target int) bool {
	rows, cols := len(matrix), len(matrix[0])
	l, r := 0, rows*cols-1

	for l <= r {
		mid := (l + r) / 2
		i, j := mid/cols, mid%cols

		if matrix[i][j] == target {
			return true
		} else if matrix[i][j] < target {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return false
}
