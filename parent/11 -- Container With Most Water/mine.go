package main

func maxArea(height []int) int {
	l, r := 0, len(height)-1
	maxArea := 0

	for l < r {
		maxArea = max(maxArea, min(height[l], height[r])*(r-l))

		if height[l] < height[r] {
			l += 1
		} else {
			r -= 1
		}
	}

	return maxArea
}
