package main

import "slices"

func uniformArray(nums1 []int) bool {
	allEven := true
	for _, num := range nums1 {
		if num%2 == 1 {
			allEven = false
			break
		}
	}
	if allEven {
		return true
	}

	if slices.Min(nums1)%2 == 1 {
		return true
	}

	return false
}
