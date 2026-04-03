package main

import "sort"

func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	events := [][2]int{}

	for _, entry := range firstList {
		events = append(events, [2]int{entry[0], 1})
		events = append(events, [2]int{entry[1], -1})
	}
	for _, entry := range secondList {
		events = append(events, [2]int{entry[0], 1})
		events = append(events, [2]int{entry[1], -1})
	}

	sort.Slice(events, func(i, j int) bool {
		if events[i][0] != events[j][0] {
			return events[i][0] < events[j][0]
		}
		return events[i][1] > events[j][1]
	})

	res := [][]int{}
	new_start := 0
	active := 0

	for _, entry := range events {
		if entry[1] == 1 {
			active++
			if active == 2 {
				new_start = entry[0]
			}
		} else {
			if active == 2 {
				res = append(res, []int{new_start, entry[0]})
			}
			active--
		}
	}

	return res
}
