package quick

import "fmt"

func main() {
	arr := []int{1, 5, 2, 3, 4, 1, 4}
	quick_sort(arr, 0, len(arr)-1)
	fmt.Println(arr)
}

func quick_sort(nums []int, left, right int) {
	// Lomuto Quick Sort
	if left >= right {
		return
	}
	pivot := right
	i := left - 1

	for j := left; j < right; j++ {
		if nums[j] < nums[pivot] {
			i++
			nums[i], nums[j] = nums[j], nums[i]
		}
	}

	i++
	nums[i], nums[pivot] = nums[pivot], nums[i]

	quick_sort(nums, left, i-1)
	quick_sort(nums, i+1, right)
}
