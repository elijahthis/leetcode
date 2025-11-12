class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        q = []

        for i, char in enumerate(s):
            count[char] = count.get(char,0) + 1
            q.append(char)
        
        for i in range(len(q)):
            if count[s[i]] == 1:
                return i
        return -1