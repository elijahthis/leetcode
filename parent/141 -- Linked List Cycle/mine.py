# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # My weird implementation of Floyd's Cycle Detection Algo. Works
        fast = slow = head
        while True:
            if slow:
                slow = slow.next
            
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            
            if slow == fast and fast != None:
                return True
            if slow == None:
                break
        return False
        