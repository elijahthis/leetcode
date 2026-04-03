class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Time: O(m + n)
        # Space: O(k); k = no. of intesections
        """
        2 pointer
        For each pair of intervals, the intersection exists when they overlap. The intersection is:
        [max(a.start, b.start), min(a.end, b.end)]
        """

        res = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            x1, y1 = firstList[i]
            x2, y2 = secondList[j]

            lo, hi = max(x1, x2), min(y1, y2)

            if lo <= hi:
                res.append([lo, hi])
            
            if y1 < y2:
                i += 1
            else:
                j += 1
        return res