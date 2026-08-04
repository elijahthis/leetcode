class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack (Same as before, simpler)
        # Time: O(n)
        # Space: O(n)
        res = [0] * len(temperatures)
        stack = []  # idx, temp

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx, _ = stack.pop()
                res[idx] = i - idx

            stack.append((i, temp))
            
        return res