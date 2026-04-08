package main

import "slices"

func maxProduct(nums []int) int {
	res, min_so_far, max_so_far := nums[0], nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		candidates := []int{nums[i], nums[i] * min_so_far, nums[i] * max_so_far}
		min_so_far = slices.Min(candidates)
		max_so_far = slices.Max(candidates)
		res = max(max_so_far, res)
	}

	return res
}
