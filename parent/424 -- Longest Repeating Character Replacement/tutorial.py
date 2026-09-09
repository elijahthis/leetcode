class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time: O(n)
        # Space: O(1) auxillary space (dict holds a max of 26 items)
        # Learn: https://gemini.google.com/app/948809c304fdddb3

        charCount = {}
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            # 1. Add new character to window
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            
            # 2. Update historical max frequency
            max_freq = max(max_freq, charCount[s[r]])
            
            # 3. If window is invalid, slide the whole window (don't shrink)
            if (r - l + 1) - max_freq > k:
                charCount[s[l]] -= 1
                l += 1
                
        # The window size at the end is exactly the maximum valid size found
        return len(s) - l