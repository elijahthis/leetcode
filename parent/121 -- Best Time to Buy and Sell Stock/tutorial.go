package main

func maxProfit(prices []int) int {
	i, max_profit := 0, 0
	j := 1

	for j < len(prices) {
		diff := prices[j] - prices[i]
		if diff > 0 {
			max_profit = max(max_profit, diff)
			j++
		} else {
			i = j
			j++
		}
	}
	return max_profit
}
