package main

func trap(height []int) int {
	l, r := 0, len(height)-1
	max_left, max_right := height[l], height[r]
	trapped_water := 0

	for l < r {
		if max_left < max_right {
			l += 1
			max_left = max(max_left, height[l])
			trapped_water += max_left - height[l]
		} else {
			r -= 1
			max_right = max(max_right, height[r])
			trapped_water += max_right - height[r]
		}
	}
	return trapped_water
}
