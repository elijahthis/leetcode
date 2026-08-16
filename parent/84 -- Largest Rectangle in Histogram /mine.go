package main

func largestRectangleArea(heights []int) int {
	n := len(heights)
	var res int
	var boundaries [][2]int
	for range n {
		boundaries = append(boundaries, [2]int{-1, n})
	}

	//  forward pass
	forward_stack := []int{0}
	i := 1
	for i < n {
		if heights[i] >= heights[forward_stack[len(forward_stack)-1]] {
			forward_stack = append(forward_stack, i)
			i += 1
			continue
		}
		for len(forward_stack) > 0 && heights[i] < heights[forward_stack[len(forward_stack)-1]] {
			idx := forward_stack[len(forward_stack)-1]
			forward_stack = forward_stack[:len(forward_stack)-1]
			boundaries[idx][1] = i
		}
		forward_stack = append(forward_stack, i)
	}

	//  backward pass
	backward_stack := []int{n - 1}
	i = n - 1
	for i >= 0 {
		if heights[i] >= heights[backward_stack[len(backward_stack)-1]] {
			backward_stack = append(backward_stack, i)
			i -= 1
			continue
		}
		for len(backward_stack) > 0 && heights[i] < heights[backward_stack[len(backward_stack)-1]] {
			idx := backward_stack[len(backward_stack)-1]
			backward_stack = backward_stack[:len(backward_stack)-1]
			boundaries[idx][0] = i
		}
		backward_stack = append(backward_stack, i)
	}

	for i := range n {
		l, r := boundaries[i][0], boundaries[i][1]
		area := heights[i] * (r - l - 1)
		res = max(res, area)
	}

	return res
}
