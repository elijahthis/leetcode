class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Time: O(2ⁿ) → O(n³) with memoization
        # Space: O(n) recursion depth

        word_set = set(wordDict)  # O(1) lookup
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for subsentence in backtrack(end):
                        sentences.append((word + " " + subsentence).strip())
            
            memo[start] = sentences
            return sentences

        return backtrack(0)
