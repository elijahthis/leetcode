"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # ANALYSIS:
        # - create a hashmap to store the mapping between the old and new nodes
        # - iterate through the linked list and create a new node for each node
        # - store the mapping in the hashmap
        # - iterate through the linked list again and update the next and random pointers of the new nodes
        # - return the head of the new linked list
        # - O(n) time complexity
        # - O(n) space complexity
        
        curr = head
        hashMap = {}   # old_node -> new_node

        while curr:
            hashMap[curr] = Node(curr.val)
            curr = curr.next
        
        copy = hashMap.get(head, None)
        curr = head
        curr_copy = copy

        while curr:
            curr_copy.next = hashMap.get(curr.next, None)
            curr_copy.random = hashMap.get(curr.random, None)

            curr = curr.next
            curr_copy = curr_copy.next

        return copy



