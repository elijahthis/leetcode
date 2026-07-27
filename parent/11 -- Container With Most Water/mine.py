class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Greedy 2-Ptr (also happens to be Neetcode's)
        # Time: O(n)
        # Space: O(1)

        l,r = 0, len(height)-1
        maxArea = 0

        while l < r:
            width = r-l
            maxArea = max(maxArea, min(height[l], height[r]) * width)
            
            # we move in the one that's less, bcos we might still find sth that's bigger than the bigger one
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
    
# Time Complexity: O(n)
# Space Complexity: O(1)