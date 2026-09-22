package main

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev, curr *ListNode
	curr = head
	for curr != nil {
		nxt := curr.Next
		curr.Next = prev
		prev = curr
		curr = nxt
	}
	return prev
}
func reorderList(head *ListNode) {
	fast, slow := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	tail := reverseList(slow)
	for tail.Next != nil {
		nxt := head.Next
		head.Next = tail
		tail = tail.Next
		head.Next.Next = nxt
		head = head.Next.Next
	}
	tail.Next = nil
}
