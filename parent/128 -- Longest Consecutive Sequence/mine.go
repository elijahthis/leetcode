package main

func longestConsecutive(nums []int) int {
	res, start, end := 0, 0, 0
	nums_set, visited := map[int]bool{}, map[int]bool{}
	for _, num := range nums {
		if !nums_set[num] {
			nums_set[num] = true
		}
	}

	for num := range nums_set {
		if !visited[num] {
			visited[num] = true
			start, end = num, num

			for nums_set[start-1] {
				start--
				visited[start] = true
			}
			for nums_set[end+1] {
				end++
				visited[end] = true
			}

			res = max(res, end-start+1)
		}
	}

	return res
}
