import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # heap + dedup (Dijkstra/BFS-style)
        # Time: O(nlogn)
        # Space: O(nuy)

        seen = set([1])
        heap = [1]
        heapq.heapify(heap)
        res = 1

        for _ in range(n):
            val = heapq.heappop(heap)
            res = val

            for x in [2,3,5]:
                new_val = val*x
                if new_val not in seen:
                    heapq.heappush(heap, new_val)
                    seen.add(new_val)
        
        return res