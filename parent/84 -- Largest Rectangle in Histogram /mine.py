class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        n = len(heights)
        boundaries = [[-1, n] for _ in range(n)]   # (l,r)
        res = 0

        # forward pass (find right boundary)
        forward_stack = [0]
        i = 1
        while i < n:
            if heights[i] >= heights[forward_stack[-1]]:
                forward_stack.append(i)
                i += 1
                continue
            
            while forward_stack and heights[i] < heights[forward_stack[-1]]:
                idx = forward_stack.pop()
                boundaries[idx][1] = i
            forward_stack.append(i)
        
        # backward pass (find left boundary)
        backward_stack = [n-1]
        i = n-2
        while i >= 0:
            if heights[i] >= heights[backward_stack[-1]]:
                backward_stack.append(i)
                i -= 1
                continue
            
            while backward_stack and heights[i] < heights[backward_stack[-1]]:
                idx = backward_stack.pop()
                boundaries[idx][0] = i
            backward_stack.append(i)

        for i in range(n):
            l,r = boundaries[i]
            area = heights[i] * (r - l - 1)
            res = max(res, area)
        return res


