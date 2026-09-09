package main

func characterReplacement(s string, k int) int {
	l, maxFreq := 0, 0
	charCount := map[uint8]int{}

	for r, _ := range s {
		count := 0
		if c, exists := charCount[s[r]]; exists {
			count = c
		}
		charCount[s[r]] = count + 1

		maxFreq = max(maxFreq, charCount[s[r]])

		if r-l+1-maxFreq > k {
			charCount[s[l]] -= 1
			l += 1
		}
	}

	return len(s) - l
}
