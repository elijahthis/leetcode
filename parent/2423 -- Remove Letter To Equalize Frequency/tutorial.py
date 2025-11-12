from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Time: O(26 * n) ≈ O(n)
        # Space: O(26) = O(1) constant extra space.

        freq = Counter(word)
        
        for char in list(freq.keys()):
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]

            if len(set(freq.values())) == 1:
                return True
            
            freq[char] = freq.get(char, 0) + 1
        
        return False
