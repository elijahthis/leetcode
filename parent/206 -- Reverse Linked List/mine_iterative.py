# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # Simple iterative solution. Optimal
        # Time: O(n). 
        # Space: O(1)
        curr = head
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        
        return prev