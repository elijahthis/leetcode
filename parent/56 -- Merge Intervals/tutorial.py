class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) time complexity because of sorting
        # O(n) space complexity because we are storing the result

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]] # start with the first interval

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                # if it overlaps
                result[-1][1] = max(lastEnd, end) # find the max in case of cases like [1, 5], [2, 4]
            else:
                result.append([start, end]) # if it doesn't overlap, add it to the result
        
        return result