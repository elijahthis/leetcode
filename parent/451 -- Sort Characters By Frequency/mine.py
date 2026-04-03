import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        heap = []
        res = []

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        
        for key, val in counts.items():
            heapq.heappush(heap, (val*-1, key))

        while heap:
            ch = heapq.heappop(heap)
            res.append(ch[1]*(ch[0]*-1))
        
        return "".join(res)