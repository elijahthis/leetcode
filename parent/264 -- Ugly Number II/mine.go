package main

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func nthUglyNumber(n int) int {
	h := &IntHeap{1}
	heap.Init(h)

	seen := map[int]bool{1: true}
	res := 0

	primes := [3]int{2, 3, 5}

	for _ = range n {
		val := heap.Pop(h).(int)
		res = val

		for _, k := range primes {
			new_val := val * k
			if !seen[new_val] {
				heap.Push(h, new_val)
				seen[new_val] = true
			}
		}
	}

	return res
}
