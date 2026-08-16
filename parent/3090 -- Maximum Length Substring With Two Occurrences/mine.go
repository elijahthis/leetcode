package main

func maximumLengthSubstring(s string) int {
	res, l := 0, 0
	counts := map[string]int{}

	for r := range len(s) {
		counts[string(s[r])] += 1

		for counts[string(s[r])] > 2 {
			counts[string(s[l])] -= 1
			l += 1
		}

		res = max(res, r-l+1)
	}

	return res
}
