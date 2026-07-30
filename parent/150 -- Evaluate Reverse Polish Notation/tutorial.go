package main

import "strconv"

func evalRPN(tokens []string) int {
	apply := func(op string, op1, op2 int) int {
		switch op {
		case "+":
			return op1 + op2
		case "-":
			return op1 - op2
		case "*":
			return op1 * op2
		case "/":
			return op1 / op2
		default:
			return 0
		}
	}

	var stack []int
	operations := map[string]struct{}{
		"+": struct{}{},
		"-": struct{}{},
		"*": struct{}{},
		"/": struct{}{},
	}

	for _, char := range tokens {
		if _, exists := operations[char]; exists {
			op2 := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			op1 := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			stack = append(stack, apply(char, op1, op2))
		} else {
			val, err := strconv.Atoi(char)
			if err != nil {
				return 0
			}
			stack = append(stack, val)
		}
	}
	return stack[len(stack)-1]
}
