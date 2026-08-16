package main

func remainingMethods(n int, k int, invocations [][]int) []int {
	adjList := map[int][]int{}
	infected := map[int]bool{}
	var res []int

	for _, invo := range invocations {
		node, nei := invo[0], invo[1]
		adjList[node] = append(adjList[node], nei)
	}

	var dfs_infect func(node int)
	dfs_infect = func(node int) {
		infected[node] = true

		for _, nei := range adjList[node] {
			if _, exists := infected[nei]; !exists {
				dfs_infect(nei)
			}
		}
	}

	dfs_infect(k)

	for _, invo := range invocations {
		node, nei := invo[0], invo[1]
		_, nodeExists := infected[node]
		_, neiExists := infected[nei]
		if !nodeExists && neiExists {
			for i := range n {
				res = append(res, i)
			}
			return res
		}

	}
	for i := range n {
		if _, exists := infected[i]; !exists {
			res = append(res, i)
		}
	}
	return res
}
