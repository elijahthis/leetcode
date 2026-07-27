from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # BFS
        # Time: O(n)
        # Space: O(2n) ≈ O(n)

        q = deque([start])
        visited = {start}

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            left, right = curr - arr[curr], curr + arr[curr]
            if left >= 0 and left not in visited:
                q.append(left)
                visited.add(left)
            if right < len(arr) and right not in visited:
                q.append(right)
                visited.add(right)
            
        return False
