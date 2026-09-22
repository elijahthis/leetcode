package main

import "container/list"

func maxSlidingWindow(nums []int, k int) []int {
	var res []int
	dq := list.New()

	for r := range nums {
		if dq.Len() > 0 && dq.Front().Value.(int) < r-k+1 {
			// popleft
			fr := dq.Front()
			dq.Remove(fr)
		}
		for dq.Len() > 0 && nums[dq.Back().Value.(int)] < nums[r] {
			// popright
			ba := dq.Back()
			dq.Remove(ba)
		}

		dq.PushBack(r)

		if r >= k-1 {
			res = append(res, nums[dq.Front().Value.(int)])
		}

	}
	return res
}
