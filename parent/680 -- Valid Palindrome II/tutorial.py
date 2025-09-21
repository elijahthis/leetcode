class Solution:
    # ANALYSIS:
        # - The time complexity is O(n) where n is the length of the string
        # - The space complexity is O(n) where n is the length of the string
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        while l <= r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            l+= 1
            r -= 1
        return True