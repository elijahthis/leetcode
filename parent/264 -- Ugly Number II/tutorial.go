func nthUglyNumber(n int) int {
	dp := make([]int, n)
	dp[0] = 1
	p2, p3, p5 := 0, 0, 0

	for i := 1; i < n; i++ {
		val2 := dp[p2] * 2
		val3 := dp[p3] * 3
		val5 := dp[p5] * 5

		dp[i] = min(val2, val3, val5)

		if dp[i] == val2 {
			p2++
		}
		if dp[i] == val3 {
			p3++
		}
		if dp[i] == val5 {
			p5++
		}
	}

	return dp[n-1]
}