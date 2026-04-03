package main

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	res := [][]int{}
	i, j := 0, 0

	for i < len(firstList) && j < len(secondList) {
		x1, y1 := firstList[i][0], firstList[i][1]
		x2, y2 := secondList[j][0], secondList[j][1]

		lo, hi := max(x1, x2), min(y1, y2)

		if lo <= hi {
			res = append(res, []int{lo, hi})
		}

		if y1 < y2 {
			i++
		} else {
			j++
		}
	}

	return res
}
