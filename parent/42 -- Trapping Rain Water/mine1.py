class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n^2). TLE Creative, correct, inefficient and a bit complicated
        # Space: O(n)
        """
        You look for a left boundary (stack_l).

        You scan forward for a right boundary (stack_r) that is at least as tall as the left boundary.

        If you can't find one, you fall back to the highest bar you saw along the way (maxInd).

        The water trapped is the rectangular area between them (min(left, right) * distance) minus the height of the blocks in between.
        """

        stack_l = stack_r = 0
        res = i = 0

        # start with non-zero
        while i < len(height) and height[i] == 0:
            i += 1
        
        if i < len(height):
            stack_l = i
            i += 1
        
        while i < len(height):
            pref_sum_hash = {}
            while i < len(height) and height[i] >= height[stack_l]:
                stack_l = i
                i += 1

            # now our stack starts with valid left boundary
            maxInd = i      # This rewind makes it O(n^2)
            # populate stack till right boundary
            stack_r = stack_l
            while i < len(height) and height[i] < height[stack_l]:
                stack_r = i
                pref_sum_hash[i] = pref_sum_hash.get(i-1, 0) + height[i]
                if height[i] > height[maxInd]:
                    maxInd = i
                i += 1
            if i < len(height) and height[i] >= height[stack_l]:
                stack_r = i
                i += 1

            # couldn't find a bigger right bound
            if height[stack_r] < height[stack_l]:
                i = maxInd
                stack_r = maxInd
                i += 1
            
            # process stack
            water_height = min(height[stack_l], height[stack_r])
            stack_size = max(stack_r - stack_l - 1, 0)
            if stack_size > 0:
                res += ((water_height*stack_size) - pref_sum_hash.get(stack_r-1, 0))

            stack_l = stack_r = i-1
        
        return res
            