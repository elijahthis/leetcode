class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack (Same as before, simpler)
        # Time: O(n)
        # Space: O(n) - Less space per stack entry
        res = [0] * len(temperatures)
        stack = []  # idx - Only store idx, since we can always retrieve temp from aray

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx

            stack.append(i)
            
        return res