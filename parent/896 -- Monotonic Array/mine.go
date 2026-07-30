package main

func isMonotonic(nums []int) bool {
	isIncr := 0

	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			if isIncr == -1 {
				return false
			}
			isIncr = 1
		} else if nums[i] < nums[i-1] {
			if isIncr == 1 {
				return false
			}
			isIncr = -1
		}
	}

	return true
}
