class Solution:
    def decodeString(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)

        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(substr * int(k))

        return "".join(stack)