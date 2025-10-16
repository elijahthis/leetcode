# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Time: O(N)
        # Space: O(H)
        # GPT says it's fastest, but not on Leetcode for some reason
        
        def dfs(node: Optional[TreeNode], curr: int):
            if not node:
                return
            
            curr =  curr * 10 + node.val

            if not node.left and not node.right:
                return curr
            
            return dfs(node.left, curr) + dfs(node.right, curr)
            

        return dfs(root, 0)