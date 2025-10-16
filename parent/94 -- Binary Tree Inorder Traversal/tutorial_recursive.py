# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # most efficient
        # recursive solution
        # Time: O(n)
        # Space: O(H)     -> H = height of tree
        res = []

        def inorder(root: Optional[TreeNode]):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return res