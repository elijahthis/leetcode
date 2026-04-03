package main

func missingNumber(nums []int) int {
	res := len(nums)

	for i := range len(nums) {
		res += i - nums[i]
	}
	return res
}
