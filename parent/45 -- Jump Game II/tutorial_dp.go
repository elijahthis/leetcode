package main

import "math"

func jump(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	for i := range n {
		dp[i] = math.MaxInt
	}

	dp[0] = 0

	for i := range n {
		for step := 1; step <= nums[i]; step++ {
			if i+step < n {
				dp[i+step] = min(dp[i+step], dp[i]+1)
			}
		}
	}

	return dp[len(dp)-1]
}
