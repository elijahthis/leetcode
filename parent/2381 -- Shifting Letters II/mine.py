class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Right idea. Too complicated. too much wasted work
        # Time: O(n)
        
        events = {}
        diffArr = [0] * len(s)

        for l, r, v in shifts:
            val = 1 if v == 1 else -1
            events[l] = events.get(l, 0) + val
            events[r + 1] = events.get(r + 1, 0) - val

        diffs = []
        curr = 0
        prev = None

        for x in sorted(events):
            if prev is not None and prev <= x - 1:
                diffs.append([prev, x - 1, curr])
            curr += events[x]
            prev = x

        
        res = []

        for l,r,v in diffs:
            for i in range(l, r+1):
                diffArr[i] = v

        for i,v in enumerate(diffArr):
            res.append(chr(((ord(s[i])+v-97)%26) + 97))


        return "".join(res)