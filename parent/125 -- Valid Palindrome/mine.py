class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ANALYSIS:
        # - We need to check if the string is a palindrome
        # - We can ignore the non-alphanumeric characters
        # - We can ignore the case of the characters
        # - We can use two pointers to check if the string is a palindrome
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        stack = ""

        for char in s:
            if char.isalnum():
                stack = stack + char.lower()
        
        l, r = 0, len(stack)-1

        while l < r:
            if stack[l] == stack[r]:
                l += 1
                r -= 1
            else: return False
        return True