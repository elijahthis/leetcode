from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #charCount -> list

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
            
            res[tuple(count)].append(word)

        return list(res.values())
    
"""
Time Complexity: O(n * k)

Space Complexity: O(n * k)
----------------
1. Count array for each word: O(26) → O(1) (constant space per word).
2. Hashmap stores up to n keys in worst case: O(n).
   Each key is a tuple of size 26 → O(26n) → O(n).
3. Result stores all input words grouped: O(n * k).

=> Overall: O(n * k)
"""