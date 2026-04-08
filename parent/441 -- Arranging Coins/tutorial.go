package main

func arrangeCoins(n int) int {
	l, r := 1, n

	for l <= r {
		k := (l + r) / 2
		coins_needed := (k * (k + 1)) / 2

		if coins_needed == n {
			return k
		} else if coins_needed < n {
			l = k + 1
		} else {
			r = k - 1
		}
	}
	return r
}
