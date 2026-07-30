class Solution:
    def trap(self, height: List[int]) -> int:
        # Two-pointer
        # Time: O(n)
        # Space: O(1)

        l, r = 0, len(height)-1
        max_left, max_right = height[l], height[r]
        trapped_water = 0

        while l < r:
            # The water level is determined by the shorter of the two maximums
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                trapped_water += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                trapped_water += max_right - height[r]
        
        return trapped_water