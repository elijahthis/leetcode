import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []

        heapq.heappush(rooms, intervals[0][1])

        for s,e in intervals[1:]:
            if s >= rooms[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, e)
        
        return len(rooms)
 
        
# [[0,30],[5,10],[15,20]]

# rooms -> [15, 30]