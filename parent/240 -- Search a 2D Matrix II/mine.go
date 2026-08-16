package main

func searchMatrix(matrix [][]int, target int) bool {
	for _, row := range matrix {
		if row[0] <= target && row[len(row)-1] >= target {
			l, r := 0, len(matrix[0])-1
			for l <= r {
				mid := (l + r) / 2
				if row[mid] == target {
					return true
				} else if row[mid] < target {
					l = mid + 1
				} else {
					r = mid - 1
				}
			}
		}
	}
	return false
}
