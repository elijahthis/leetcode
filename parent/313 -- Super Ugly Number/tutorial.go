package main

import "slices"

func nthSuperUglyNumber(n int, primes []int) int {
	dp := make([]int, n)
	dp[0] = 1
	next_multiples := make([]int, len(primes))
	idx := make([]int, len(primes))
	for i := range len(primes) {
		next_multiples[i] = primes[i]
		idx[i] = 0
	}

	for i := 1; i < n; i++ {
		dp[i] = slices.Min(next_multiples)

		for j := 0; j < len(primes); j++ {
			if dp[i] == next_multiples[j] {
				idx[j]++
				next_multiples[j] = dp[idx[j]] * primes[j]
			}
		}
	}
	return dp[len(dp)-1]
}
