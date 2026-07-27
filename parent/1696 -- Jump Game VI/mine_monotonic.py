from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Monotonic Deque Soln.
        # passes, confusing
        
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        minQ = deque([(nums[0], 0)])
        maxQ = deque([(nums[0], 0)])
        
        for i in range(1,n):
            while minQ and minQ[-1][1] < i-k:
                minQ.pop()
            while maxQ[0][1] < i-k:
                maxQ.popleft()

            dp[i] = nums[i] + max(maxQ[0][0], minQ[-1][0])
            
            while minQ and dp[i] < minQ[-1][0]:
                minQ.pop()
            while maxQ and dp[i] > maxQ[-1][0]:
                maxQ.pop()

            maxQ.append((dp[i], i))
            minQ.append((dp[i], i))
        
        return dp[-1]