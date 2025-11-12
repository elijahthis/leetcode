class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        duplicates = set()
        q = []

        for i, char in enumerate(s):
            if char in count:
                duplicates.add(char)
            count[char] = count.get(char,0) + 1
            q.append(char)
        
        for i in range(len(q)):
            if s[i] not in duplicates:
                return i
        return -1
            