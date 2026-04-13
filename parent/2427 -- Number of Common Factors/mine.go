package main

func commonFactors(a int, b int) int {
	res := 0

	for i := range min(a, b) {
		if a%(i+1) == 0 && b%(i+1) == 0 {
			res++
		}
	}
	return res
}
