class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Traditional Monotonic Stack approach. More optimal for space
        # Time: O(n)
        # Space: O(n)

        n = len(heights)
        stack = [(0, heights[0])]     # (idx, height)
        areas = []
        i = 1
        res = 0

        while i < n:
            if heights[i] >= heights[i-1]:
                stack.append((i, heights[i]))
                i += 1
                continue
            
            idx = 0
            while stack and stack[-1][1] >= heights[i]:
                idx, num = stack.pop()
                res = max(res, num * (i - idx))
            
            stack.append((idx, heights[i]))
            i += 1
        
        for idx, num in stack:
            res = max(res, num * (n - idx))
        
        return res