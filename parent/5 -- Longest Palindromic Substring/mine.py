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

        for i in range(len(s)):
            # check odd length
            l = r = i
            curr = s[i]
            while l >=0 and r < len(s) and s[l] == s[r]:
                if l < r:
                    curr = s[l] + curr + s[r]
                l -=1
                r +=1
            
            if len(curr) >= len(res):
                res = curr
                resLen = len(curr)

            # check even length
            l, r = i, i+1
            curr = ""
            while l >=0 and r < len(s) and s[l] == s[r]:
                curr = s[l] + curr + s[r]
                l -=1
                r +=1
            
            if len(curr) >= len(res):
                res = curr
        
        return res
