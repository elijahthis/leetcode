class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Cleaner and slightly easier to reason about
        # Time: O(n)
        # Space: O(n)

        max_len = 0
        hashS = set()

        l, r = 0,0
        while r < len(s):
            while s[r] in hashS:
                hashS.remove(s[l])
                l += 1
            
            hashS.add(s[r])
            r += 1
            max_len = max(max_len, r-l)
        return max_len
