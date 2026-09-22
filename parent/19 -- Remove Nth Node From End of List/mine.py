# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # simple iterative reversal
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Time: O(n)    3 passes, though
        # Space: O(1)
        # 1. Reverse list
        rev = self.reverseList(head)

        # 2. Iterate normally and remove
        ptr = 1
        curr = rev
        prev = None
        while curr and ptr < n:
            prev = curr
            curr = curr.next
            ptr += 1
        
        if prev:
            prev.next = curr.next
        else:
            rev = rev.next  # handle edge case of removing head (or rather, tail)
        # curr.next = None

        # Reverse and return
        return self.reverseList(rev)