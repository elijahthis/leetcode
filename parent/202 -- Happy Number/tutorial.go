package main

func isHappy(n int) bool {
	visited := map[int]bool{}

	_, isVisited := visited[n]

	for n != 1 && !isVisited {
		visited[n] = true

		total := 0
		for n != 0 {
			digit := n % 10
			total += digit * digit
			n /= 10
		}
		n = total

		_, isVisited = visited[n]
	}
	return n == 1
}
