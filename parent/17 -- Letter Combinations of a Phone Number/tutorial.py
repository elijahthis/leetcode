class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking problem
        # Time Complexity: O(n · 4^n)
        # Space Complexity: O(n · 4^n)

        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtrack(i: int, currStr: str):
            # base case
            if len(currStr) == len(digits):
                result.append(currStr)
                return
            
            for char in digitsToChar[digits[i]]:
                backtrack(i+1, currStr+char)

        if digits:  
            backtrack(0, "")
        return result
