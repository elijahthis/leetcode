class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n)
        # Works, and very fast, but too convoluted with repeated work 
        # Two-pass, but still fastest
        if not intervals or newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        xn, yn = newInterval
        for i in range(len(intervals)):
            x1,y1 = intervals[i]

            if x1 <= xn <= y1 or (xn <= x1 and yn >= x1):
                intervals[i] = [min(x1, xn), max(y1, yn)]
                break
        
        res = [intervals[0]]
        for i,j in intervals:
            if xn > res[-1][1] and yn < i:
                res.append([xn, yn])

            if i <= res[-1][1]:
                res[-1][1] = max(res[-1][1], j)
            else:
                res.append([i,j])

        return res