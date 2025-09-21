# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Constant Space solution
        # use a fast and slow pointer to find the middle

        fast,slow = head,head

        # find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check if palindrome
        left,right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True


# Time Complexity: O(n)
# Space Complexity: O(1) - Constant space