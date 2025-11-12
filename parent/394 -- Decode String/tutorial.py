class Solution:
    def decodeString(self, s: str) -> str:
        # ANALYSIS:
        # - We can use a stack to keep track of the characters in the string
        # - We can iterate through the string and push each character onto the stack
        # - When we encounter a closing bracket, we can pop the characters until we reach an opening bracket
        # - We can then pop the opening bracket and the characters before the opening bracket to get the substring
        # - We can then pop the digits before the substring to get the number of times the substring should be repeated
        # - We can then push the substring repeated the number of times onto the stack
        # - We can then join the characters in the stack to get the decoded string
        # - The time complexity is O(n) where n is the length of the string
        # - The space complexity is O(n) where n is the length of the string
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                
                stack.append(substr * int(k))
        
        return "".join(stack)
