package main

func twoSum(nums []int, target int) []int {
	prevHash := make(map[int]int)

	for i, num := range nums {
		rem := target - num
		if _, exists := prevHash[rem]; exists {
			return []int{i, prevHash[rem]}
		}
		prevHash[num] = i
	}
	return []int{}
}
