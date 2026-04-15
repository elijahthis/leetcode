class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # classic Greedy interval scheduling variant
        # If no overlap → keep the interval
        # If overlap → remove one interval (increment res)
        # When overlapping → keep the interval with the smaller end time (greedy choice)
        # Time: O(nlogn)
        # Space: O(1)

        intervals.sort()
        lastEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start < lastEnd: # if overlap
                res += 1        # remove one interval (increment res)
                lastEnd = min(lastEnd, end) # keep the interval with the smaller end time (greedy choice)
            else:
                lastEnd = end

        return res