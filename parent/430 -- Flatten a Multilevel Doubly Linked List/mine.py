"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # ANALYSIS:
        # Time: O(n)
        # Space: O(n)
        # We use a stack to keep track of the nodes that we need to visit later

        # We iterate through the linked list
        # If we see a node with a child, we add the next node to the stack
        # We set the next node to the child node
        # We set the child node's prev to the current node
        # We set the child node to None
        # If we see a node with no next node and there are nodes in the stack
        # We pop the next node from the stack
        # We set the current node's next to the next node
        # We set the next node's prev to the current node
        # We return the head node
        # Depth First Search
        stack = []

        curr = head

        # We iterate through the linked list
        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)     # We add the next node to the stack (keep it for later)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            elif not curr.next and len(stack) > 0:    # when we run out of nexts, we pop from the stack
                pending_node = stack.pop()
                curr.next = pending_node
                pending_node.prev = curr

            curr = curr.next
        
        return head
        