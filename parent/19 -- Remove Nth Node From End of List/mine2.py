# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # 2 Pointer approach (faster. 1 pass)
        # Time: O(n)    1 pass
        # Space: O(1)
        dummy = ListNode(0, head)
        left = right = dummy
        for _ in range(n+1):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next