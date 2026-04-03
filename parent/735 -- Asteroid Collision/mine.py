class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Collision-based question
        # Time: O(n). Optimal
        # Space: O(n)
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    # pop
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroid):
                    # skip
                    break
                else:
                    # pop and skip
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack