package main

func resultArray(nums []int) []int {
	arr1, arr2 := []int{nums[0]}, []int{nums[1]}
	var res []int

	for i := 2; i < len(nums); i++ {
		if arr1[len(arr1)-1] > arr2[len(arr2)-1] {
			arr1 = append(arr1, nums[i])
		} else {
			arr2 = append(arr2, nums[i])
		}
	}

	res = append(arr1, arr2...)
	return res
}
