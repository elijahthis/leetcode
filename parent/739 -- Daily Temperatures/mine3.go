package main

func dailyTemperatures(temperatures []int) []int {
	var stack []int
	res := make([]int, len(temperatures))

	for i, temp := range temperatures {
		for len(stack) > 0 && temp > temperatures[stack[len(stack)-1]] {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[idx] = i - idx
		}
		stack = append(stack, i)
	}

	return res
}
