package main

import "strings"

func shiftingLetters(s string, shifts []int) string {
	total := 0
	res := make([]string, len(shifts))
	for _, num := range shifts {
		total += num
	}

	for i, cha := range s {
		res = append(res, string(((int(cha)+total-97)%26)+97))
		total -= shifts[i]
	}
	return strings.Join(res, "")
}
