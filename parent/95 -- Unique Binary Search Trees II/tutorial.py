# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(l, r) -> List[Optional[TreeNode]]:
            if l == r:
                return [TreeNode(l)]
            if l > r:
                return [None]
            
            res = []
            for val in range(l, r+1):
                for leftTree in generate(l, val-1):
                    for rightTree in generate(val+1, r):
                        node = TreeNode(val, leftTree, rightTree)
                        res.append(node)
            return res
        
        return generate(1, n)