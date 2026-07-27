from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS 
        # Time: O(n)
        # Space: O(n) -- Optimized for space by removing visited set

        q = deque([start])

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True
            
            if arr[curr] < 0:
                continue
            

            left, right = curr - arr[curr], curr + arr[curr]
            if left >= 0:
                q.append(left)
            if right < len(arr):
                q.append(right)
            
            # OPTIMIZATION: Use the original array as visited set. Store -ve value at each visited index
            arr[curr] = -arr[curr]
            
        return False
