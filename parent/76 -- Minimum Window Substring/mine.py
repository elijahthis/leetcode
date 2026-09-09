class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Correct and Clever and Elegant
        # Time: O(N*U), where U = no. of unique chars in t. Basically O(N) where U is 52
        # Space: O(U) or O(1)

        source_counts = {}
        window_counts = {}
        l = 0
        res = None

        # populate source map
        for char in t:
            source_counts[char] = source_counts.get(char, 0) + 1
        
        for r in range(len(s)):
            window_counts[s[r]] = window_counts.get(s[r], 0) + 1
            if r-l+1 < len(t):
                # don't do anything until we have a window large enough
                continue

            # check if window is valid
            isValid = True
            for key in source_counts.keys():
                if source_counts[key] > window_counts.get(key, 0):
                    isValid = False
                    break
            
            if isValid:
                # shrink window to min. acceptable window
                while isValid:
                    # move l
                    window_counts[s[l]] -= 1
                    if window_counts[s[l]] == 0:
                        del window_counts[s[l]]
                    l += 1

                    # check validity of smaller window
                    for key in source_counts.keys():
                        if source_counts[key] > window_counts.get(key, 0):
                            isValid = False
                            break
                res = [l-1, r]      # store min. acceptable window
            elif res:
                # prevents us from processing any new windows larger than our curent minimum
                window_counts[s[l]] -= 1
                if window_counts[s[l]] == 0:
                    del window_counts[s[l]]
                l += 1
            
        return s[res[0]:res[1]+1] if res else ""