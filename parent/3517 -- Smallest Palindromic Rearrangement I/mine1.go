package main

import (
	"slices"
	"strings"
)

func smallestPalindrome(s string) string {
	n := len(s)
	sl := strings.Split(s, "")[:n/2]
	slices.Sort(sl)

	rev_sl := slices.Clone(sl)
	slices.Reverse(rev_sl)

	if n%2 == 0 {
		return strings.Join(slices.Concat(sl, rev_sl), "")
	}
	return strings.Join(slices.Concat(sl, []string{string(s[n/2])}, rev_sl), "")
}
