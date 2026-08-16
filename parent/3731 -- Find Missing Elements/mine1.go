package main

func findMissingElements(nums []int) []int {
	minim, maxim := 100, 0
	hashSet := map[int]bool{}
	var res []int
	for _, x := range nums {
		minim = min(minim, x)
		maxim = max(maxim, x)
		hashSet[x] = true
	}
	for x := minim; x <= maxim; x++ {
		if _, exists := hashSet[x]; !exists {
			res = append(res, x)
		}
	}

	return res
}
