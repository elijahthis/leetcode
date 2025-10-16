# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Time: O(n)
        # Space: O(n)

        if not nums:
            return None
        
        
        if len(nums) == 1:
            root = TreeNode(nums[0])
        else:
            mid = len(nums) // 2

            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            if mid < len(nums)-1:
                root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root