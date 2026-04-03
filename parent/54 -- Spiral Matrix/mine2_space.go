package main

func spiralOrder(matrix [][]int) []int {
	left, right := 0, len(matrix[0])-1
	top, bottom := 0, len(matrix)-1
	res := make([]int, 0, len(matrix)*len(matrix[0]))

	for left <= right && top <= bottom {
		// left -> right
		for y := left; y <= right; y++ {
			res = append(res, matrix[top][y])
		}
		top++

		// top -> bottom
		for x := top; x <= bottom; x++ {
			res = append(res, matrix[x][right])
		}
		right--

		// right -> left
		if top <= bottom {
			for y := right; y >= left; y-- {
				res = append(res, matrix[bottom][y])
			}
			bottom--
		}

		// bottom -> top
		if left <= right {
			for x := bottom; x >= top; x-- {
				res = append(res, matrix[x][left])
			}
			left++
		}
	}

	return res
}
