package main

func predictTheWinner(nums []int) bool {
	n := len(nums)
	var dp [][]int
	for i := range n {
		dp = append(dp, []int{})
		for j := range n {
			if i == j {
				dp[i] = append(dp[i], nums[i])
			} else {
				dp[i] = append(dp[i], 0)
			}
		}
	}

	for length := 2; length <= n; length++ {
		for i := range n - length + 1 {
			j := i + length - 1

			pickLeft := nums[i] - dp[i+1][j]
			pickRight := nums[j] - dp[i][j-1]

			dp[i][j] = max(pickLeft, pickRight)
		}
	}

	return dp[0][n-1] >= 0
}
