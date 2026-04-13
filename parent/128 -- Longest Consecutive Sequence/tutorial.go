package main

func longestConsecutive(nums []int) int {
	longest := 0
	nums_set := map[int]bool{}
	for _, num := range nums {
		if !nums_set[num] {
			nums_set[num] = true
		}
	}

	for num := range nums_set {
		if !nums_set[num-1] {
			length := 1
			for nums_set[num+length] {
				length++
			}
			longest = max(longest, length)
		}
	}

	return longest
}
