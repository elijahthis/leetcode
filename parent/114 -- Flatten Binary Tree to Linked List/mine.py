# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Most Optimal
        # Space: O(n)
        # Time: O(n)

        ls = [root]

        def preorder(node: Optional[TreeNode]):
            if not node:
                return
            
            ls.append(node)

            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        for i, node in enumerate(ls):
            if node:
                node.left = None

                if i < len(ls)-1:
                    node.right = ls[i+1]
                else:
                    node.right = None
                