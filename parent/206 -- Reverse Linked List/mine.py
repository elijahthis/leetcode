# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """ CORRECT, Optimal, Beats 100% of submissions
        Passes all test cases
        Mine is better than NeetCode's solution
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        if head:
            next_node = head.next
        else:
            next_node = None

        while next_node:
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
            next_node = curr_node.next
        
        if curr_node:
            curr_node.next = prev_node
        return curr_node
