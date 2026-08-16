package main

import "slices"

type Pair struct {
	Pos   int
	Speed int
}

func carFleet(target int, position []int, speed []int) int {
	n := len(position)
	var newArr []Pair
	for i := range n {
		newArr = append(newArr, Pair{
			Pos:   position[i],
			Speed: speed[i],
		})
	}
	slices.SortFunc(newArr, func(a, b Pair) int {
		if a.Pos < b.Pos {
			return -1
		} else if a.Pos > b.Pos {
			return 1
		} else {
			return 0
		}
	})

	res := 1

	eta := float64((target - newArr[n-1].Pos)) / float64(newArr[n-1].Speed)
	for i := n - 2; i >= 0; i-- {
		curr_eta := float64((target - newArr[i].Pos)) / float64(newArr[i].Speed)
		if curr_eta <= eta {
			continue
		}

		eta = curr_eta
		res += 1
	}
	return res
}
