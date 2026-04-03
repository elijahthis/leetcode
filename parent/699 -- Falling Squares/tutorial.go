package main

func fallingSquares(positions [][]int) []int {
	intervals := [][3]int{}
	heights := []int{}

	for _, posit := range positions {
		left, size, right := posit[0], posit[1], posit[0]+posit[1]
		maxHeight := 0

		for _, inter := range intervals {
			l, r, h := inter[0], inter[1], inter[2]
			if !(l >= right || r <= left) {
				maxHeight = max(maxHeight, h)
			}
		}

		currHeight := size + maxHeight
		intervals = append(intervals, [3]int{left, right, currHeight})
		if len(heights) > 0 {
			heights = append(heights, max(currHeight, heights[len(heights)-1]))
		} else {
			heights = append(heights, currHeight)
		}
	}

	return heights
}
