package main

func lengthOfLongestSubstring(s string) int {
	maxLen, l, r := 0, 0, 0
	hashSet := map[uint8]bool{}

	for r < len(s) {
		for {
			_, exists := hashSet[s[r]]
			if !exists {
				break
			}
			delete(hashSet, s[l])
			l += 1
		}
		hashSet[s[r]] = true
		r += 1
		maxLen = max(maxLen, r-l)
	}

	return maxLen
}
