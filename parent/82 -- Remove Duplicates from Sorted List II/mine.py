# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)

        if not head:
            return None
            
        prev = None
        curr = head
        currVal = head.val

        while curr:
            hasMoved = False
            while curr.next and curr.next.val == currVal:
                hasMoved = True
                curr = curr.next
            if hasMoved:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next

            if not hasMoved:
                prev = curr
            curr = curr.next
            if curr:
                currVal = curr.val
        
        return head
