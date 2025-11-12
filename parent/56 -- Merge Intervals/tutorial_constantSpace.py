class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        write = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[write][1]:
                intervals[write][1] = max(intervals[write][1], intervals[i][1])
            else:
                write += 1
                intervals[write] = intervals[i]
        
        return intervals[:write+1]

