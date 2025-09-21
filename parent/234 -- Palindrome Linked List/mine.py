# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # use array for stack instead of string
        # because string concatenation in Python is O(k) each time
        # and can result in O(n2) solutions
        vals = [] 
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        l,r = 0,len(vals)-1
        while l<r:
            if vals[l] != vals[r]:
                return False
            l += 1
            r -= 1
        return True


# Time Complexity: O(n)
# Space Complexity: O(n)