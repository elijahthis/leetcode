# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ANALYSIS:
        # Approach:
        # 1. Traverse through the tree using a recursive function
        # 2. At each node, check if the current node's value is within the range of the left and right values
        # 3. If the current node's value is not within the range, return False
        # 4. If the current node's value is within the range, recursively check the left and right subtrees
        # 5. Return the result of the recursive calls
        # Time complexity: O(n) where n is the number of nodes in the tree
        # Space complexity: O(n) where n is the number of nodes in the tree

        def valid(node, left, right):
            
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
           
        return valid(root, float("-inf"), float("inf"))