package main

func maxSubarrayLength(nums []int, k int) int {
	res := 1
	counts := map[int]int{nums[0]: 1}
	l, r := 0, 1

	for l <= r && r < len(nums) {
		lastVal, exists := counts[nums[r]]
		if !exists {
			lastVal = 0
		}
		counts[nums[r]] = lastVal + 1

		for l <= r && counts[nums[r]] > k {
			counts[nums[l]] -= 1
			l += 1
		}

		res = max(res, r-l+1)
		r += 1
	}
	return res
}
