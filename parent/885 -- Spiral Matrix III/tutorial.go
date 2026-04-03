package main

func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
	directions := [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	res := [][]int{{rStart, cStart}}
	x, y := rStart, cStart
	steps := 1

	for len(res) < rows*cols {
		for i := range 4 {
			dx, dy := directions[i][0], directions[i][1]
			for _ = range steps {
				x += dx
				y += dy

				if 0 <= x && x < rows && 0 <= y && y < cols {
					res = append(res, []int{x, y})
				}
			}

			if i%2 == 1 {
				steps++
			}
		}
	}

	return res
}
