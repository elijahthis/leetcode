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
        
        stack_str = ""      # remaining strings
        stack_counts = []   # [[char, count]]
        
        for i, char in enumerate(s):
            stack_str = stack_str + char

            if len(stack_counts) > 0 and stack_counts[-1][0] == char:
                stack_counts[-1][1] = stack_counts[-1][1] + 1
            else:
                stack_counts.append([char, 1])

            if len(stack_str) >= k and stack_counts[-1][1] == k:
                stack_str = stack_str[:-k]
                stack_counts.pop()
        
        return stack_str

