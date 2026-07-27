
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Time: O(n)
        # Space: O(n) (visited + recursion stack)

        visited = set()

        def dfs(i):
            if arr[i] == 0:
                return True
            visited.add(i)

            left = i - arr[i]
            if left >= 0 and left not in visited and dfs(left):
                return True
            
            right = i + arr[i]
            if right < len(arr) and right not in visited and dfs(right):
                return True

            return False

        return dfs(start)
