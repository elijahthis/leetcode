from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic Queue
        # Time: O(N)
        # Space: O(N)
        res = []
        q = deque()  # Stores *indices*, not the actual values
        
        for r in range(len(nums)):
            # 1. Clean up the front: remove the index if it falls out of the current window
            if q and q[0] < r - k + 1:
                q.popleft()
                
            # 2. Clean up the back: remove indices whose values are smaller than the incoming value
            # This maintains the strictly decreasing (monotonic) property
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            # 3. Add the current element's index to the back of the deque
            q.append(r)
            
            # 4. Once our window reaches size k, the maximum is always at the front
            if r >= k - 1:
                res.append(nums[q[0]])
                
        return res