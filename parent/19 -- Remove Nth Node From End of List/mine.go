package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var curr, prev *ListNode
	curr = head
	for curr != nil {
		nxt := curr.Next
		curr.Next = prev
		prev = curr
		curr = nxt
	}
	return prev
}
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	rev := reverseList(head)

	var curr, prev *ListNode
	curr = rev
	for range n - 1 {
		prev = curr
		curr = curr.Next
	}
	if prev != nil {
		prev.Next = curr.Next
	} else {
		rev = rev.Next
	}
	curr.Next = nil

	return reverseList(rev)
}
