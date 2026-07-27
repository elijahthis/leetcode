from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Monotonic Deque Soln.
        # Time: O(n)
        # Space: O(n)

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        # dq stores tuples of (dp_value, index)
        # It is strictly monotonically decreasing.
        dq = deque([(nums[0], 0)])
        
        for i in range(1, n):
            # 1. Remove elements that have fallen out of our window of size 'k'
            while dq and dq[0][1] < i - k:
                dq.popleft()
                
            # 2. The front of the deque is guaranteed to be the max in the window
            dp[i] = nums[i] + dq[0][0]
            
            # 3. Maintain the monotonic decreasing property before adding dp[i]
            # We pop smaller values from the right because they are useless now
            # (dp[i] is newer and larger/equal)
            while dq and dq[-1][0] <= dp[i]:
                dq.pop()
                
            # 4. Add current step to the deque
            dq.append((dp[i], i))
            
        return dp[-1]