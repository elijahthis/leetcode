package main

import "math"

func maxSlidingWindow(nums []int, k int) []int {
	// Time: O(Nk). Passes Python, TLE Go
	// Space: O(k)
	var res []int
	l, curr_max := 0, math.MinInt
	counts := map[int]int{}

	for r := range nums {
		counts[nums[r]] = counts[nums[r]] + 1
		if r-l+1 < k {
			curr_max = max(curr_max, nums[r])
			continue
		}

		if nums[r] >= curr_max {
			curr_max = nums[r]
		} else if counts[curr_max] == 0 {
			val := math.MinInt
			for key, _ := range counts {
				val = max(val, key)
			}
			curr_max = val
		}

		res = append(res, curr_max)

		counts[nums[l]] -= 1
		if counts[nums[l]] == 0 {
			delete(counts, nums[l])
		}
		l += 1
	}
	return res
}
