package main

import "slices"

func minEatingSpeed(piles []int, h int) int {
	l, r := 1, slices.Max(piles)
	res := r

	for l <= r {
		mid := (l + r) / 2
		hours := 0
		for _, p := range piles {
			hours += ((p + mid - 1) / mid) //  ceil division
		}

		if hours <= h {
			res = min(res, mid)
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return res
}
