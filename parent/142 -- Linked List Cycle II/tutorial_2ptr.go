package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	slow, fast := head, head
	crossed := false

	for fast != nil && fast.Next != nil {
		slow, fast = slow.Next, fast.Next.Next

		if slow == fast {
			crossed = true
			break
		}
	}
	if !crossed {
		return nil
	}

	for head != slow {
		head, slow = head.Next, slow.Next
	}

	return slow
}
