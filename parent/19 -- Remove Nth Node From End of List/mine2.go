package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummy := &ListNode{
		Val:  0,
		Next: head,
	}
	left, right := dummy, dummy

	for range n + 1 {
		right = right.Next
	}

	for right != nil {
		left = left.Next
		right = right.Next
	}

	left.Next = left.Next.Next

	return dummy.Next
}
