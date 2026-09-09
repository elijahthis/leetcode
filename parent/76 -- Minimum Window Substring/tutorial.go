package main

import "math"

func minWindow(s string, t string) string {
	if s == "" || t == "" {
		return ""
	}

	source_counts := map[uint8]int{}
	for i := range t {
		source_counts[t[i]] = source_counts[t[i]] + 1
	}

	have, need := 0, len(source_counts)
	window_counts := map[uint8]int{}
	res, res_len := []int{-1, -1}, math.MaxInt
	l := 0

	for r := range s {
		char := s[r]
		window_counts[char] = window_counts[char] + 1
		if source_counts[char] > 0 && window_counts[char] == source_counts[char] {
			have += 1
		}

		for have == need {
			if r-l+1 < res_len {
				res = []int{l, r}
				res_len = r - l + 1
			}

			left_char := s[l]
			window_counts[left_char] -= 1
			if source_counts[left_char] > 0 && window_counts[left_char] < source_counts[left_char] {
				have -= 1
			}

			l += 1
		}

	}
	if res_len != math.MaxInt {
		return s[res[0] : res[1]+1]
	}
	return ""
}
