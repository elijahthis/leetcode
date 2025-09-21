class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # ANALYSIS:
        # Approach:
        # 1. Create a stack to store the characters and their counts
        # 2. Traverse through the string
        # 3. At each character, check if the current character is the same as the previous character
        # 4. If the current character is the same as the previous character, increment the count
        # 5. If the count reaches k, remove the last k characters from the stack
        # 6. Continue until the end of the string
        # 7. Return the remaining characters in the stack
        # Time complexity: O(n) where n is the length of the string
        # Space complexity: O(n) where n is the length of the string
        stack = []  # [char, count]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                    stack.pop()
        
        return "".join(char * count for char, count in stack)
