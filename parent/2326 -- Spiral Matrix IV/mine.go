package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
	top, bottom := 0, m-1
	left, right := 0, n-1

	res := make([][]int, m)
	for i := range m {
		res[i] = make([]int, n)
		for j := range n {
			res[i][j] = -1
		}
	}

	for head != nil && top <= bottom && left <= right {
		for y := left; y <= right; y++ {
			if head == nil {
				break
			}
			res[top][y] = head.Val
			head = head.Next
		}
		top++

		for x := top; x <= bottom; x++ {
			if head == nil {
				break
			}
			res[x][right] = head.Val
			head = head.Next
		}
		right--

		if top <= bottom {
			for y := right; y >= left; y-- {
				if head == nil {
					break
				}
				res[bottom][y] = head.Val
				head = head.Next
			}
			bottom--
		}

		if left <= right {
			for x := bottom; x >= top; x-- {
				if head == nil {
					break
				}
				res[x][left] = head.Val
				head = head.Next
			}
			left++
		}
	}

	return res
}
