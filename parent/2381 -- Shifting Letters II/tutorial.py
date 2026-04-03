class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Sweep Line-ish (diff array) + Prefix Sum
        # 1D diff array
        # Time: O(n+k)
        # Space: O(n)

        n = len(s)
        diffs = [0] * len(s)
        
        # build diff array
        for l, r, v in shifts:
            val = 1 if v == 1 else -1
            diffs[l] += val
            if r+1 < n:
                diffs[r+1] -= val

        # prefix sum + build result
        res = []
        curr = 0

        for i in range(n):
            curr += diffs[i]
            res.append(chr(((ord(s[i]) - ord("a") + curr) % 26) + ord("a")))

        return "".join(res)
        