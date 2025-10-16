from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # RECURSIVE
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp
    
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



# create a list of 0s with 10 items dynamically
# [0] * 10


        