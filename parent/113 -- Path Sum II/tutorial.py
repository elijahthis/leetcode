# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Time: O(n)
        # Space: O(H)
        # most optimal

        res = []
        
        def dfs(node: Optional[TreeNode], currSum: int, currArr: List[int]):
            if not node:
                return
            
            currSum += node.val
            currArr.append(node.val)
            
            if not node.left and not node.right and currSum == targetSum:
                res.append(currArr.copy())      # copy only at leaf
                # No return

            dfs(node.left, currSum, currArr)    # remove copies
            dfs(node.right, currSum, currArr)   # remove copies

            currArr.pop()       # backtracking
            
        dfs(root, 0, [])
        return res
