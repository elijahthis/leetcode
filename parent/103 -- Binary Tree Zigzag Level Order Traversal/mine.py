import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        ind = 0
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if ind%2 == 1:
                        level.insert(0, node.val)
                    else:
                        level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
            ind += 1
        
        return res