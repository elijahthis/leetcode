class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:   # only runs if while didn't break
            return None
        
        # key part. See Floyd's Cycle algo detection proof
        while head != slow:
            head, slow = head.next, slow.next
        return slow