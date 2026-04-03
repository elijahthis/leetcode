class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Correct / well-known implementation of Floyd's Cycle Detection Algo
        # Mental Model
        # - If there's a cycle → fast laps slow → they meet
        # - If no cycle → fast hits None → terminate
        # Time: O(n)
        # Space: O(1)

        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False