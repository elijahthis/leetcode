package main

func minWindow(s string, t string) string {
	source_counts := map[uint8]int{}
	window_counts := map[uint8]int{}
	l := 0
	var res []int

	for i := range t {
		source_counts[t[i]] = source_counts[t[i]] + 1
	}

	for r := range s {
		window_counts[s[r]] = window_counts[s[r]] + 1
		if r-l+1 < len(t) {
			continue
		}

		isValid := true
		for key, _ := range source_counts {
			if window_counts[key] < source_counts[key] {
				isValid = false
				break
			}
		}

		if isValid {
			for isValid {
				window_counts[s[l]] -= 1
				if window_counts[s[l]] == 0 {
					delete(window_counts, s[l])
				}
				l += 1

				for key, _ := range source_counts {
					if window_counts[key] < source_counts[key] {
						isValid = false
						break
					}
				}
			}
			res = []int{l - 1, r}
		} else if res != nil {
			window_counts[s[l]] -= 1
			if window_counts[s[l]] == 0 {
				delete(window_counts, s[l])
			}
			l += 1
		}
	}
	if res != nil {
		return s[res[0] : res[1]+1]
	}
	return ""
}
