import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Time: O(n log n)
        # Space: O(n)
        # max-heap + sorted event list + Sweep Line
        res = []
        events = sorted(
            [(l,-h,r) for l,r,h in buildings] + # start events
            [(r,0,0) for l,r,h in buildings])   # end events
        heap = [(0, float('inf'))] # (neg_height, end_x)
        
        prev_maxH = 0

        for l, neg_h, r in events:
            if neg_h:   # start event
                heapq.heappush(heap, (neg_h,r))
            
            while l >= heap[0][1]:  # evict expired buildings
                heapq.heappop(heap)
            
            curr_maxH = -heap[0][0]
            if curr_maxH != prev_maxH:  # update skyline when max height changes (up or down)
                res.append([l, curr_maxH])
                prev_maxH = curr_maxH
        
        return res