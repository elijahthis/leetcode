class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashes = {} # sorted_word -> result_ind

        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in hashes:
                ind = hashes.get(sorted_word, 0)
                result[ind].append(word)
            else:
                hashes[sorted_word] = len(result)
                result.append([word])

        return result

"""    
Time Complexity:
---------------
Let:
- n = number of words in strs
- k = maximum length of a single word

1. Sorting each word: O(k log k)
2. Doing this for n words: O(n * k log k)
3. Lookup/insert in hashmap (hashes): O(1) average case

=> Overall: O(n * k log k)

Space Complexity:
----------------
1. Hashmap stores up to n keys (in worst case when no words are anagrams): O(n * k) 
   (since each key is a string of length k)
2. Result list stores all words grouped: O(n * k)

=> Overall: O(n * k)
"""