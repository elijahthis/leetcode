package main

import (
	"slices"
)

func smallestPalindrome(s string) string {
	n := len(s)

	first := []byte(s[:n/2])
	slices.Sort(first)

	ans := make([]byte, 0, n)
	ans = append(ans, first...)

	if n%2 == 1 {
		ans = append(ans, s[n/2])
	}

	for i := len(first) - 1; i >= 0; i-- {
		ans = append(ans, first[i])
	}

	return string(ans)
}
