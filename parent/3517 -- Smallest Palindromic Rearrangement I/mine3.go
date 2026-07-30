package main

import (
	"strings"
)

func smallestPalindrome(s string) string {
	var freq [26]int
	var res []string
	var mid string

	for _, char := range s {
		freq[int(char)-int('a')] += 1
	}

	for i, count := range freq {
		char := string(i + int('a'))
		if count > 0 {
			res = append(res, strings.Repeat(char, count/2))
			if count%2 == 1 {
				mid = char
			}
		}
	}

	res = append(res, mid)

	for i := len(freq) - 1; i >= 0; i-- {
		count := freq[i]
		char := string(i + int('a'))

		if count > 0 {
			res = append(res, strings.Repeat(char, count/2))
		}
	}

	return strings.Join(res, "")
}
