class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Counting Sort. Most efficient
        # Time: O(n)
        # Space: O(1)

        freq = [0] * 26
        res = []
        mid = ''

        for char in s:
            freq[ord(char)-ord('a')] += 1
        
        for i, count in enumerate(freq):
            char = chr(i + ord('a'))
            if count > 0: 
                res.append(char * (count//2))
                if count%2 == 1:
                    mid = char
        
        return ''.join(res + [mid] + res[::-1])