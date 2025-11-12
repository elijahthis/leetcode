# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Time: O(N)
        # Space: O(W)
        
        total = 0
        stack = [(root, 0)]

        while stack:
            node, curr = stack.pop()
            curr = curr * 10 + node.val

            if not node.left and not node.right:
                total += curr

            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))
        

        return total
            

