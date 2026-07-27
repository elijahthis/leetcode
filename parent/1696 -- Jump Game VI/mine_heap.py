import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Heap solution
        # Time: O(n log n)
        # Space: O(n)
        
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        maxH = [(-nums[0], 0)]     # [(dp_value, index)]
        
        for i in range(1,n):
            while maxH[0][1] < i-k:
                heapq.heappop(maxH)

            dp[i] = nums[i]-maxH[0][0]
            heapq.heappush(maxH, (-dp[i], i))
                
        return dp[-1]