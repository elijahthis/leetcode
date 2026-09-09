class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        source_counts = {}
        for char in t:
            source_counts[char] = source_counts.get(char, 0) + 1
            
        window_counts = {}
        have, need = 0, len(source_counts)
        
        res, res_len = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the character added meets the exact requirement in t, increment 'have'
            if char in source_counts and window_counts[char] == source_counts[char]:
                have += 1
                
            # While the window is valid, try to shrink it from the left
            while have == need:
                # Update our result if this window is smaller than our previous best
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                    
                # Pop the left character from our window
                left_char = s[l]
                window_counts[left_char] -= 1
                
                # If removing this character breaks our valid window, decrement 'have'
                if left_char in source_counts and window_counts[left_char] < source_counts[left_char]:
                    have -= 1
                    
                l += 1
                
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""