class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time:  O(S) --> Worst case
        # Space: O(1)
        
        res = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            j = 0
            while j < min(len(word), len(res)) and res[j] == word[j]:
                j += 1
            
            res = res[:j]
        return res
