package main

type Pair struct {
	L int
	R int
}

func predictTheWinner(nums []int) bool {
	memo := make(map[Pair]int)
	var total int
	for _, num := range nums {
		total += num
	}

	var dfs func(l, r int) int
	dfs = func(l, r int) int {
		if val, exists := memo[Pair{l, r}]; exists {
			return val
		}

		if l == r {
			return nums[l]
		}
		if l > r {
			return 0
		}

		memo[Pair{l, r}] = max(
			min(nums[l]+dfs(l+2, r), nums[l]+dfs(l+1, r-1)),
			min(nums[r]+dfs(l, r-2), nums[r]+dfs(l+1, r-1)),
		)
		return memo[Pair{l, r}]
	}

	return (total - dfs(0, len(nums)-1)) <= total/2
}
