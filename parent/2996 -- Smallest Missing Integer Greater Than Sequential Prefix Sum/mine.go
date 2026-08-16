package main

func missingInteger(nums []int) int {
	n := len(nums)
	i := 1
	total := nums[0]
	hashSet := map[int]bool{}

	for _, num := range nums {
		hashSet[num] = true
	}

	for i < n && nums[i] == nums[i-1]+1 {
		total += nums[i]
		i += 1
	}

	for {
		if _, exists := hashSet[total]; !exists {
			return total
		}
		total += 1
	}
}
