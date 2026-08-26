package main

import (
	"container/heap"
	"math"
)

type HeapEntry struct {
	Price     int
	Timestamp int
}

// min-heap implementation
type MinHeap []HeapEntry

func (h MinHeap) Len() int { return len(h) }
func (h MinHeap) Less(i, j int) bool {
	if h[i].Price == h[j].Price {
		return h[i].Timestamp < h[j].Timestamp
	}
	return h[i].Price < h[j].Price
}
func (h MinHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(HeapEntry))
}
func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// max-heap implementation
type MaxHeap []HeapEntry

func (h MaxHeap) Len() int { return len(h) }
func (h MaxHeap) Less(i, j int) bool {
	if h[i].Price == h[j].Price {
		return h[i].Timestamp > h[j].Timestamp
	}
	return h[i].Price > h[j].Price
}
func (h MaxHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(HeapEntry))
}
func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type StockPrice struct {
	Prices      map[int]int // timestamp -> price
	MinHeap     *MinHeap
	MaxHeap     *MaxHeap
	LastUpdated int
}

func Constructor() StockPrice {
	minH := &MinHeap{}
	maxH := &MaxHeap{}
	heap.Init(minH)
	heap.Init(maxH)

	return StockPrice{
		Prices:      map[int]int{},
		MinHeap:     minH,
		MaxHeap:     maxH,
		LastUpdated: math.MinInt,
	}

}

func (this *StockPrice) Update(timestamp int, price int) {
	entry := HeapEntry{
		Price:     price,
		Timestamp: timestamp,
	}
	heap.Push(this.MinHeap, entry)
	heap.Push(this.MaxHeap, entry)

	this.LastUpdated = max(this.LastUpdated, timestamp)
	this.Prices[timestamp] = price
}

func (this *StockPrice) Current() int {
	return this.Prices[this.LastUpdated]
}

func (this *StockPrice) Maximum() int {
	for this.Prices[(*this.MaxHeap)[0].Timestamp] != (*this.MaxHeap)[0].Price {
		heap.Pop(this.MaxHeap)
	}
	return (*this.MaxHeap)[0].Price
}

func (this *StockPrice) Minimum() int {
	for this.Prices[(*this.MinHeap)[0].Timestamp] != (*this.MinHeap)[0].Price {
		heap.Pop(this.MinHeap)
	}
	return (*this.MinHeap)[0].Price
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Update(timestamp,price);
 * param_2 := obj.Current();
 * param_3 := obj.Maximum();
 * param_4 := obj.Minimum();
 */
