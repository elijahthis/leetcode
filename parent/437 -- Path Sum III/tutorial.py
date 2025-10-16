class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}  # Stores how many times a prefix sum has occurred
        
        def dfs(node, currSum):
            if not node:
                return 0
            
            # 1️⃣ Update the running sum
            currSum += node.val
            
            # 2️⃣ Count valid paths ending at this node
            # If currSum - targetSum exists in prefix,
            # it means there's a previous prefixSum such that
            # (currSum - previous) = targetSum
            count = prefix.get(currSum - targetSum, 0)
            
            # 3️⃣ Add current sum to prefix map
            prefix[currSum] = prefix.get(currSum, 0) + 1
            
            # 4️⃣ Explore children
            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)
            
            # 5️⃣ Backtrack — remove current sum before returning
            prefix[currSum] -= 1
            
            return count
        
        return dfs(root, 0)
