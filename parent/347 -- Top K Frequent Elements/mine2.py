import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n + m log k) — O(n) to count, O(m log k) for heap ops, where m ≤ n
        # Space: O(m + k) — dict plus heap
        # Probably best for interviews

        counts = {}
        heap = []

        for n in nums:
            counts[n] = counts.get(n,0) + 1
        
        for key, val in counts.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n[1] for n in heap]
        