package main

func shiftingLetters(s string, shifts [][]int) string {
	n := len(s)
	diffs := make([]int, n)

	for _, shift := range shifts {
		l, r, v := shift[0], shift[1], shift[2]
		val := 1
		if v == 0 {
			val = -1
		}
		diffs[l] += val
		if r+1 < n {
			diffs[r+1] -= val
		}
	}

	res := make([]byte, n)
	curr := 0
	shifted := 0
	for i := range s {
		curr += diffs[i]
		shifted = (int(s[i]-'a') + curr) % 26
		if shifted < 0 {
			shifted += 26
		}
		res[i] = byte((shifted + 'a'))
	}
	return string(res)
}
