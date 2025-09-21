class Solution:
    # ANALYSIS:
        # - The time complexity is O(n) where n is the length of the string
        # - The space complexity is O(n) where n is the length of the string
        # helper function method saves space, but use string reversal to checck palindromeness
        
    def barePalindrome(self, stack: str) -> bool:
        l,r = 0,len(stack)-1
        while l <= r:
            if stack[l] == stack[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def validPalindrome(self, s: str) -> bool:
        stack = ''.join([c.lower() for c in s if c.isalnum()])
        
        l,r = 0,len(stack)-1
        while l <= r:
            if stack[l] == stack[r]:
                l += 1
                r -= 1
            else:
                return self.barePalindrome(stack[l:r]) or self.barePalindrome(stack[l+1:r+1])
        return True