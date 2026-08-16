class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        
        res = l = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            while counts[s[r]] > 2:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res