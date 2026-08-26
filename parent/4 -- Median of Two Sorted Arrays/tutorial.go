package main

import "math"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// In Python, floor division  rounds down towards negative infinity.
	// In Go, integer division truncates towards zero.
	// This distinction destroys the index-based binary search you are using when l + r becomes negative:
	// In Python: -1 // 2 evaluates to -1.
	// In Go: -1 / 2 evaluates to 0.

	A, B := nums1, nums2
	if len(A) > len(B) {
		A, B = B, A
	}

	m, n := len(A), len(B)

	// l and r now represent the NUMBER of elements taken from A for the left partition.
	l, r := 0, m

	// +1 ensures that if the total length is odd, the left partition
	// gets the extra element.
	halfLen := (m + n + 1) / 2

	for l <= r {
		i := (l + r) / 2
		j := halfLen - i

		aLeft := math.MinInt
		if i > 0 {
			aLeft = A[i-1]
		}
		aRight := math.MaxInt
		if i < m {
			aRight = A[i]
		}

		bLeft := math.MinInt
		if j > 0 {
			bLeft = B[j-1]
		}
		bRight := math.MaxInt
		if j < n {
			bRight = B[j]
		}

		// Valid partition found
		if aLeft <= bRight && bLeft <= aRight {

			// Odd total length: the median is exactly the max of the left side
			if (m+n)%2 == 1 {
				return float64(max(aLeft, bLeft))
			}

			// Even total length: average the max of left and min of right
			return float64(max(aLeft, bLeft)+min(aRight, bRight)) / 2.0

		} else if aLeft > bRight {
			// A's left partition is too large, move our boundary left
			r = i - 1
		} else {
			// A's left partition is too small, move our boundary right
			l = i + 1
		}
	}

	return 0
}
