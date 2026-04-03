package main

import "fmt"

func main() {
	arr := []int{1, 5, 2, 3, 4, 1, 4}
	insertion_sort(arr)
	fmt.Println(arr)
}

func insertion_sort(nums []int) {
	for i := 1; i < len(nums); i++ {
		key := nums[i]
		j := i - 1

		for j >= 0 && key < nums[j] {
			nums[j+1] = nums[j]
			j--
		}
		nums[j+1] = key
	}
}
