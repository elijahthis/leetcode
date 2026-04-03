class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        res = []
        for i, cha in enumerate(s):
            res.append(chr(((ord(cha)+total-97)%26) + 97))
            total -= shifts[i]
        
        return "".join(res)