package main

func merge_sort(arr []int) []int {
	if len(arr) > 1 {
		mid := len(arr) / 2
		left, right := merge_sort(arr[:mid]), merge_sort(arr[mid:])

		return merge(left, right)
	}
	return arr
}

func merge(left []int, right []int) []int {
	i, j := 0, 0
	res := []int{}

	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			res = append(res, left[i])
			i++
		} else {
			res = append(res, right[j])
			j++
		}
	}

	res = append(res, left[i:]...)
	res = append(res, right[j:]...)
	return res
}
