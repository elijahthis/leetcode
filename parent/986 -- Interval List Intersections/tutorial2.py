class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Uses the Sweep Line Algorithm
        # Time: O((m + n)log(m + n))
        # Space: O(m + n)
        events = []

        for l, r in firstList:
            events.append((l, 1))
            events.append((r, -1))
        for l, r in secondList:
            events.append((l, 1))
            events.append((r, -1))
        
        events.sort(key=lambda x: (x[0], -x[1]))
        
        res = []
        active = 0
        new_start = 0

        for pos, typ in events:
            if typ == 1:
                active += 1
                if active == 2:
                    new_start = pos
            else:
                if active == 2:
                    res.append([new_start, pos])
                active -= 1
        
        return res