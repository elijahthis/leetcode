import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n log k) (since each push/pop is O(log k), and we do it n times).
        # Space: O(k) (heap stores only k elements).
        
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        
	    # micro-optimization: avoid unnecessary push/pop
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, num)
        #     elif num > heap[0]:
        #         heapq.heappush(heap, num)
        #         heapq.heappop(heap)
        
        return heap[0]
    
        
    


        # built-in nlargest function
        # O(n log k) time and uses O(k) space
        #  return heapq.nlargest(k, nums)
