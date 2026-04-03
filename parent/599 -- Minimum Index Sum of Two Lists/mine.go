package main

import "math"

func findRestaurant(list1 []string, list2 []string) []string {
	hashM := map[string]int{}
	total := math.Inf(1)
	res := []string{}

	for idx, word := range list1 {
		hashM[word] = idx
	}

	for idx, word := range list2 {
		if val, exists := hashM[word]; exists {
			if float64(val+idx) < total {
				total = float64(val + idx)
				res = []string{word}
			} else if float64(val+idx) == total {
				res = append(res, word)
			}
		}
	}

	return res
}
