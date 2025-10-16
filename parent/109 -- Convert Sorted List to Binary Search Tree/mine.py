# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node = head
        ls = []
        while node:
            ls.append(node.val)
            node = node.next
        
        def helper(ls):
            if not ls:
                return None
            
            mid = len(ls) // 2
            root = TreeNode(ls[mid])

            root.left = helper(ls[:mid])
            if mid < len(ls)-1:
                root.right = helper(ls[mid+1:])

            return root
        
        return helper(ls)