package main

func generateMatrix(n int) [][]int {
	// Time: O(M*N)
	// Space: O(M*N)
	// Best time and space

	left, right := 0, n-1
	top, bottom := 0, n-1
	val := 1

	res := make([][]int, n)
	for i := range n {
		res[i] = make([]int, n)
	}

	for left <= right && top <= bottom {
		for y := left; y <= right; y++ {
			res[top][y] = val
			val++
		}
		top++

		for x := top; x <= bottom; x++ {
			res[x][right] = val
			val++
		}
		right--

		if top <= bottom {
			for y := right; y >= left; y-- {
				res[bottom][y] = val
				val++
			}
			bottom--
		}

		if left <= right {
			for x := bottom; x >= top; x-- {
				res[x][left] = val
				val++
			}
			left++
		}
	}

	return res
}
