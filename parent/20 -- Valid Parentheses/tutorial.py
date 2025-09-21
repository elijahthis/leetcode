class Solution:
    def isValid(self, s: str) -> bool:
        # ANALYSIS
        # Time: O(n)
        # Space: O(n)

        # we use a stack to keep track of the open brackets
        # we use a dictionary to map the closing brackets to the open brackets
        stack = []
        closeToOpen = {")": "(", "}":"{", "]":"["}


        # iterate through the string
        # if we see an open bracket, we add it to the stack
        # if we see a closing bracket, we check if the stack is empty
        # if it is, we return False
        # if it is not, we check if the last element in the stack is the corresponding open bracket
        # if it is, we pop it from the stack
        # if it is not, we return False
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        # if we reach the end of the string and the stack is empty, we return True
        # otherwise, we return False
        if not stack:
            return True
        return False