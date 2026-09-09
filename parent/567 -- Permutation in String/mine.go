package main

import (
	"maps"
)

func checkInclusion(s1 string, s2 string) bool {
	source_counts := map[uint8]int{}
	window_counts := map[uint8]int{}
	l := 0

	for i := range s1 {
		count := 0
		if c, exists := source_counts[s1[i]]; exists {
			count = c
		}
		source_counts[s1[i]] = count + 1
	}

	for r := range s2 {
		count := 0
		if c, exists := window_counts[s2[r]]; exists {
			count = c
		}
		window_counts[s2[r]] = count + 1

		if r-l+1 < len(s1) {
			continue
		}

		if maps.Equal(source_counts, window_counts) {
			return true
		}
		window_counts[s2[l]] -= 1
		if val := window_counts[s2[l]]; val == 0 {
			delete(window_counts, s2[l])
		}
		l += 1
	}
	return false
}
