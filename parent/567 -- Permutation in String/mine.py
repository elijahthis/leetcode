class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time: O(m+n) or O(max(m,n))
        # Space: O(1) auxillary space. (26 letters in the alphabet)

        source_counts = {}
        window_counts = {}
        l = 0

        for char in s1:
            source_counts[char] = source_counts.get(char, 0) + 1
        
        for r in range(len(s2)):
            window_counts[s2[r]] = window_counts.get(s2[r], 0) + 1

            if r-l+1 < len(s1):
                continue
            
            if window_counts == source_counts:
                return True
            window_counts[s2[l]] -= 1
            if window_counts[s2[l]] == 0:
                del window_counts[s2[l]]
            l += 1
        
        return False