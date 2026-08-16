package main

func largestRectangleArea(heights []int) int {
	n := len(heights)
	var res int
	stack := [][2]int{[2]int{0, heights[0]}} // (idx, num)

	i := 1

	for i < n {
		if heights[i] >= heights[i-1] {
			stack = append(stack, [2]int{i, heights[i]})
			i += 1
			continue
		}

		idx := 0
		for len(stack) > 0 && heights[i] < stack[len(stack)-1][1] {
			item := stack[len(stack)-1]
			idx = item[0]
			val := item[1]
			stack = stack[:len(stack)-1]

			res = max(res, val*(i-idx))
		}
		stack = append(stack, [2]int{idx, heights[i]})
		i += 1
	}
	for _, item := range stack {
		idx, val := item[0], item[1]
		res = max(res, val*(n-idx))
	}

	return res
}
