class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Time: O(2^n)
        # Space: O(n)

        word_set = set(wordDict)  # O(1) lookup
        res = []

        def backtrack(start, currStr):
            # If we've reached the end, it means all substrings were valid
            if start == len(s):
                res.append(" ".join(currStr.copy()))
                return
            
            # Try every possible end index for substring s[start:end]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    currStr.append(s[start:end])
                    backtrack(end, currStr)
                    currStr.pop()
            
        backtrack(0, [])
        return res
