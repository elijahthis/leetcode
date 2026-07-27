package main

func jump(nums []int) int {
	farthest, curr_end, jumps := 0, 0, 0
	n := len(nums)

	for i := range n - 1 {
		farthest = max(farthest, nums[i]+i)

		if i == curr_end {
			jumps++
			curr_end = farthest
		}
		if curr_end >= n {
			break
		}
	}

	return jumps
}
