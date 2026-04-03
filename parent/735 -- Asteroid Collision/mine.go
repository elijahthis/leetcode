package main

func asteroidCollision(asteroids []int) []int {
	stack := []int{}

	shouldAdd := true

	for _, asteroid := range asteroids {
		shouldAdd = true
		for len(stack) > 0 && stack[len(stack)-1] > 0 && asteroid < 0 {
			if max(stack[len(stack)-1], -stack[len(stack)-1]) < max(asteroid, -asteroid) {
				stack = stack[:len(stack)-1]
				shouldAdd = true
				continue
			} else if max(stack[len(stack)-1], -stack[len(stack)-1]) > max(asteroid, -asteroid) {
				shouldAdd = false
				break
			} else {
				stack = stack[:len(stack)-1]
				shouldAdd = false
				break
			}
		}
		if shouldAdd {
			stack = append(stack, asteroid)
		}
	}

	return stack
}
