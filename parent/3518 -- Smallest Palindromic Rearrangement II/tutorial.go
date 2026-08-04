package main

import (
	"math/big"
	"slices"
	"strings"
)

func smallestPalindrome(s string, k int) string {
	freq := make(map[rune]int)
	halfFreq := make(map[rune]int)
	var mid rune = -1 // Use -1 to represent no middle character
	var m int

	// 1. Populate frequencies using runes (handles all UTF-8 characters safely)
	for _, char := range s {
		freq[char]++
	}

	var letters []rune
	for char, count := range freq {
		if count%2 == 1 {
			mid = char
		}
		if count/2 > 0 {
			halfFreq[char] = count / 2
			m += count / 2
			letters = append(letters, char)
		}
	}

	// Sort available characters lexicographically
	slices.Sort(letters)

	// Helper to calculate factorial safely using big.Int
	factorialBig := func(n int) *big.Int {
		z := big.NewInt(1)
		z.MulRange(1, int64(n)) // If 1 > n, returns 1 natively
		return z
	}

	// 2. Calculate initial total permutations
	totalPerms := factorialBig(m)
	for _, count := range halfFreq {
		totalPerms.Div(totalPerms, factorialBig(count))
	}

	// Convert k to big.Int for safe comparisons
	kBig := big.NewInt(int64(k))
	if kBig.Cmp(totalPerms) > 0 { // if kBig > totalPerms
		return ""
	}

	halfStr := make([]rune, 0, m)

	// 3. Construct the first half character by character
	for i := 0; i < m; i++ {
		remainingLength := int64(m - i)

		for _, char := range letters {
			count := halfFreq[char]
			if count > 0 {
				// permsWithChar = (totalPerms * count) / remainingLength
				permsWithChar := new(big.Int).Mul(totalPerms, big.NewInt(int64(count)))
				permsWithChar.Div(permsWithChar, big.NewInt(remainingLength))

				if kBig.Cmp(permsWithChar) <= 0 { // if k <= permsWithChar
					halfStr = append(halfStr, char)
					halfFreq[char]--
					totalPerms = permsWithChar // Lock in this branch
					break
				} else {
					kBig.Sub(kBig, permsWithChar) // Skip branch, subtract from k
				}
			}
		}
	}

	// 4. Assemble the final palindrome string efficiently
	var builder strings.Builder
	builder.Grow(len(s)) // Pre-allocate exact memory needed

	// Write first half
	for _, ch := range halfStr {
		builder.WriteRune(ch)
	}

	// Write middle character if it exists
	if mid != -1 {
		builder.WriteRune(mid)
	}

	// Write second half (reversed first half)
	for i := len(halfStr) - 1; i >= 0; i-- {
		builder.WriteRune(halfStr[i])
	}

	return builder.String()
}