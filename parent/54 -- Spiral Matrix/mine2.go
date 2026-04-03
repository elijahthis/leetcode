package main

func spiralOrder(matrix [][]int) []int {
	M, N := len(matrix), len(matrix[0])
	visited := make(map[[2]int]bool)
	res := []int{}
	directions := [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	x, y, dirInd := 0, 0, 0

	isInSet := func(set map[[2]int]bool, val [2]int) bool {
		_, exists := set[val]
		return exists
	}

	isOutOfBounds := func(x int, y int) bool {
		return 0 > x || x >= M || 0 > y || y >= N || isInSet(visited, [2]int{x, y})
	}

	for !isOutOfBounds(x, y) {
		res = append(res, matrix[x][y])
		visited[[2]int{x, y}] = true

		new_x := x + directions[dirInd][0]
		new_y := y + directions[dirInd][1]

		if isOutOfBounds(new_x, new_y) {
			dirInd = (dirInd + 1) % 4
			new_x = x + directions[dirInd][0]
			new_y = y + directions[dirInd][1]
		}

		x = new_x
		y = new_y
	}

	return res
}
