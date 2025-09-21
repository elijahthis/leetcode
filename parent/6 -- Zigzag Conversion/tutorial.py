class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ""
        for r in range(numRows):
            increment = 2 * (numRows-1)
            for i in range(r, len(s), increment):
                # straightforward part (works perfectly for first and last)
                res += s[i]
                # get the extra characters in the middle rows
                if r != 0 and r != numRows-1 and i+increment-2*r < len(s):
                    res += s[i+increment-2*r]

        return res;