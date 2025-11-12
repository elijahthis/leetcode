from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total = 0
        queue = deque([(root, 0)])
        
        while queue:
            node, curr = queue.popleft()
            curr = curr * 10 + node.val
            
            if not node.left and not node.right:
                total += curr
            else:
                if node.left:
                    queue.append((node.left, curr))
                if node.right:
                    queue.append((node.right, curr))
        
        return total
