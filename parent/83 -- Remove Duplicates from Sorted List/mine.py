# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ANALYSIS: 
        # - Time complexity: O(n)
        # - Space complexity: O(1)
        
        prev = None
        curr = head

        while curr:
            if curr != head:
                if curr.val == prev.val:
                    prev.next = curr.next
                    curr.next = None

                    curr = prev.next
                    continue
            
            prev = curr
            curr = curr.next
        return head