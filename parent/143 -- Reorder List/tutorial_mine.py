

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative reversal
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        # Find midpoint
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse 2nd half
        tail = self.reverseList(slow)

        # loop and insert
        while tail.next:
            nxt = head.next         # temp variable
            head.next = tail
            tail = tail.next        # move tail ptr
            head.next.next = nxt
            head = head.next.next   # move head ptr
        tail.next = None    # set last tail node next ptr to null