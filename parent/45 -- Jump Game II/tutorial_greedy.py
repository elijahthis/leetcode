class Solution:
    def jump(self, nums: list[int]) -> int:
        # Greedy soln
        # Time: O(n)
        # Space: O(1)
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # We only iterate up to the second-to-last element 
        # because we don't need to jump again once we reach the end.
        for i in range(len(nums) - 1):
            # Continuously update the furthest index we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the range for our current jump...
            if i == current_jump_end:
                jumps += 1               # We are forced to make a jump
                current_jump_end = farthest  # Update our range to the furthest point found
                
                # Early exit if we can already reach the end
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps