package main

func findDuplicate(nums []int) int {
	slow, fast := 0, 0

	for {
		slow, fast = nums[slow], nums[nums[fast]]
		if slow == fast {
			break
		}
	}

	fast = 0
	for slow != fast {
		slow, fast = nums[slow], nums[fast]
	}

	return fast
}
