# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach:
        # 1. Traverse through both linked lists and store the numbers in string format
        # 2. Add the numbers and store the result in string format
        # 3. Create a new linked list and store the digits of the result in the linked list
        # 4. Return the linked list
        # Time complexity: O(n) where n is the length of the linked list
        # Space complexity: O(n) where n is the length of the linked list
        
        num_a = ""
        num_b = ""
        soln = ListNode()

        curr = l1
        while curr:
            num_a += str(curr.val)
            curr = curr.next
        
        curr = l2
        while curr:
            num_b += str(curr.val)
            curr = curr.next
        
        total = str(int(num_a) + int(num_b))

        curr = soln
        for i, digit in enumerate(total):
            curr.val = int(digit)
            if i < len(total)-1:
                curr.next = ListNode()
            else:
                curr.next = None
            
            curr = curr.next

        return soln