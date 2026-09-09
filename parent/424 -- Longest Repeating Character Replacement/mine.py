class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Correct, but slightly over-engineered
        # Time: O(n)
        # Space: O(1) auxillary space (both dicts hold a max of 26 items each)
        # Learn: https://gemini.google.com/app/948809c304fdddb3

        l = r = max_len = 0
        charCount = {}      # char -> freq,     e.g. {'A': 3, 'B': 1}
        freqCount = {}      # freq -> count,    e.g. {3: 1, 1: 1}

        while r < len(s):
            if s[r] in charCount:
                freqCount[charCount[s[r]]] -= 1
                if freqCount[charCount[s[r]]] == 0:
                    del freqCount[charCount[s[r]]]
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            freqCount[charCount[s[r]]] = freqCount.get(charCount[s[r]], 0) + 1
            r += 1

            if r-l - max(freqCount.keys()) > k:
                freqCount[charCount[s[l]]] -= 1
                if freqCount[charCount[s[l]]] == 0:
                    del freqCount[charCount[s[l]]]

                charCount[s[l]] -= 1
                if charCount[s[l]] == 0:
                    del charCount[s[l]]
                else:
                    freqCount[charCount[s[l]]] = freqCount.get(charCount[s[l]], 0) + 1
                l += 1
            else:
                max_len = max(max_len, r - l)

        return max_len


    # The Critique
    # Over-engineering: While your solution is logically sound and mathematically O(N), it is slower in practice because of overhead.
    # - Dictionary Overhead: Deleting keys, checking .get(), and calling max() on dictionary keys inside a while loop creates constant-time overhead that adds up.
    # - Unnecessary Strictness: You meticulously update freqCount when the window shrinks to ensure you always know the exact maximum frequency of the current window. You don't actually need to do this.

    # The "Historical Max" Optimization
    # In this specific problem, you only care about finding a window larger than the one you've already found. 
    # Therefore, the max_freq variable only ever needs to increase. 
    # If you shrink the window, the true max frequency of the smaller window might decrease, but it doesn't matter—you cannot possibly beat your max_len record without finding a window that has a new, higher historical max_freq.
    # Because of this, we can drop freqCount entirely.