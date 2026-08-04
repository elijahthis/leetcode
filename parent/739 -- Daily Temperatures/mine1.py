class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack
        # Time: O(n)
        # Space: O(n)
        n = len(temperatures)
        res = [0] * n
        stack = [(0, temperatures[0])] # idx, temp

        for i in range(1, len(temperatures)):
            temp = temperatures[i]
            if temp <= stack[-1][1]:
                stack.append((i, temp))
            else:
                while stack and temp > stack[-1][1]:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i, temp))
            
        return res