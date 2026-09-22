# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time: O(n)
        # Space: O(n)
        arr = []
        temp = head
        ptr = 0

        while temp:
            arr.append(temp)
            temp = temp.next
        
        half_len = len(arr) // 2
        
        # while ptr < half_len: (also works)
        while head and head.next and ptr < half_len:
            tail = arr.pop()
            arr[-1].next = None
            tail.next = head.next
            head.next = tail
            head = head.next.next
            ptr += 1