class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ANALYSIS:
        # more efficient space-wise
        # - We need to check if the string is a palindrome
        # - We can ignore the non-alphanumeric characters
        # - We can ignore the case of the characters
        # - We can use two pointers to check if the string is a palindrome
        # Time complexity: O(n)
        # Space complexity: O(1)
        

        l, r = 0, len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True