class Solution:
    # ANALYSIS:
    # - We can use a hashmap to store the values of each character.
    # - We can also use a hashmap to store the exceptions.
    # - We can iterate through the string and add the corresponding value of each character to the answer.
    # Time: O(n)
    # Space: O(1)

    def romanToInt(self, s: str) -> int:
        ans = 0
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        exceptions = {
            "I": {"V": 4, "X": 9},
            "X": {"L": 40, "C": 90},
            "C": {"D": 400, "M": 900}
            }

        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if s[i] in exceptions and s[i+1] in exceptions[s[i]]:
                    ans += exceptions[s[i]][s[i+1]]
                    i += 2
                    continue
            
            ans += values[s[i]]
            i += 1
        
        return ans