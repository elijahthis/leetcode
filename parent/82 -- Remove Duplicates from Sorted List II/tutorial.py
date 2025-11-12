class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            # If duplicates exist, skip them
            if head.next and head.val == head.next.val:
                # Move until end of duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        
        return dummy.next
