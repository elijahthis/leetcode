class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        seen = set()

        for char in s:
            if char in seen:
                seen.remove(char)
                result += 2
            else:
                seen.add(char)
        
        return result + 1 if seen else result

# Time Complexity: O(n) 

# Space Complexity:
# O(k), effectively O(1), because k <= 52
# where k = number of unique characters (at most 52 for English letters, so effectively O(1) bounded).
