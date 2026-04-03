class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n). Slow version
        # Space: O(n)
        curr = head
        visit = set()
        while curr and curr not in visit:
            visit.add(curr)
            curr = curr.next
        
        if curr == None:
            return None
        return curr
        