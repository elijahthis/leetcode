package main

func findMissingElements(nums []int) []int {
	minim, maxim := 100, 0
	var boolArr [100]int
	var res []int
	for _, x := range nums {
		minim = min(minim, x)
		maxim = max(maxim, x)
		boolArr[x-1] = 1
	}
	for x := minim; x <= maxim; x++ {
		if boolArr[x-1] == 0 {
			res = append(res, x)
		}
	}

	return res
}
