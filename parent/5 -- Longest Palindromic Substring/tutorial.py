class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ANALYSIS:
        # - We need to find the longest palindromic substring
        # - We can use two pointers to check if the string is a palindrome
        # - We can check for both odd and even length palindromes
        # - We can keep track of the longest palindrome found
        # - We're using a center expansion approach
        # Time complexity: O(n^2)
        # Space complexity: O(1)

        res = ""
        resLen = 0

        for i in range(len(s)):
            # check odd length
            l = r = i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -=1
                r +=1

            # check even length
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -=1
                r +=1
        
        return res
