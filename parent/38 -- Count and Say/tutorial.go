package main

import (
	"strconv"
	"strings"
)

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}

	var res []string
	count := 1
	prev := countAndSay(n - 1)

	for i := 1; i < len(prev); i++ {
		if prev[i] == prev[i-1] {
			count += 1
		} else {
			res = append(res, strconv.Itoa(count)+string(prev[i-1]))
			count = 1
		}
	}

	res = append(res, strconv.Itoa(count)+string(prev[len(prev)-1]))
	return strings.Join(res, "")
}
