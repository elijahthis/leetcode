package main

import (
	"container/heap"
	"math"
	"sort"
)

type IntHeap [][2]int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i][0] < h[j][0] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any) {
	*h = append(*h, x.([2]int))
}
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func getSkyline(buildings [][]int) [][]int {
	res := [][]int{}

	h := &IntHeap{[2]int{0, math.MaxInt}}
	heap.Init(h)

	events := [][3]int{}
	for _, buildi := range buildings {
		l, r, h := buildi[0], buildi[1], buildi[2]
		events = append(events, [3]int{l, h * -1, r})
		events = append(events, [3]int{r, 0, 0})
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i][0] != events[j][0] {
			return events[i][0] < events[j][0]
		} else if events[i][1] != events[j][1] {
			return events[i][1] < events[j][1]
		}
		return events[i][2] < events[j][2]
	})

	prev_maxH := 0
	for _, event := range events {
		l, neg_h, r := event[0], event[1], event[2]
		if neg_h != 0 {
			heap.Push(h, [2]int{neg_h, r})
		}
		for l >= (*h)[0][1] {
			heap.Pop(h)
		}
		curr_maxH := (*h)[0][0] * -1
		if curr_maxH != prev_maxH {
			res = append(res, []int{l, curr_maxH})
			prev_maxH = curr_maxH
		}
	}

	return res
}
