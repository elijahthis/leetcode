import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        count = collections.Counter(s)
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
        