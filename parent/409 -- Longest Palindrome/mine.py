class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        length = 0
        odd_found = False
        for freq in counts.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length
        
# Time Complexity: O(n) 

# Space Complexity:
# O(k), effectively O(1), because k <= 52
# where k = number of unique characters (at most 52 for English letters, so effectively O(1) bounded).

