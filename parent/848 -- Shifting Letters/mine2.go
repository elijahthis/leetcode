package main

func shiftingLetters(s string, shifts []int) string {
	n := len(s)
	res := make([]byte, n)
	total := 0

	for _, num := range shifts {
		total = (total + num) % 26
	}

	for i := range s {
		shift := (int(s[i]-'a') + total) % 26
		res[i] = byte(shift + 'a')
		total = (total - shifts[i]%26 + 26) % 26
	}

	return string(res)
}
