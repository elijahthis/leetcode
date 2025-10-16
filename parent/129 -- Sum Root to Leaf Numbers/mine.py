# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Really Fast
        # Time: O(N * H)
        # Space: O(L * H)
        arr = []
        res = 0

        def dfs(node: Optional[TreeNode], currArr):
            if not node:
                return
            
            currArr.append(str(node.val))

            if not node.left and not node.right:
                arr.append(currArr.copy())
            
            dfs(node.left, currArr)
            dfs(node.right, currArr)
            currArr.pop()
        
        dfs(root, [])
        for numArr in arr:
            res += int("".join(numArr))

        return res