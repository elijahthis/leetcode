package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	visited := map[*ListNode]bool{}
	_, isVisited := visited[head]

	for head != nil && !isVisited {
		visited[head] = true
		head = head.Next
		_, isVisited = visited[head]

	}
	if head == nil {
		return nil
	}
	return head
}
