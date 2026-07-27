class Solution:
    def jump(self, nums: List[int]) -> int:
        # Bottom-up DP
        # Time: O(n^2)
        # Space: O(n)
        # Passes

        n = len(nums)
        
        dp = [0] * n
        for i in range(n-2, -1, -1):
            if nums[i]:
                if i+nums[i] >= n-1:
                    dp[i] = 1
                else:
                    leastVal = float('inf')
                    for j in range(i+1, i+nums[i]+1):
                        if dp[j]:
                            leastVal = min(leastVal, dp[j])

                    dp[i] = 0 if leastVal == float('inf') else leastVal+1
            else:
                dp[i] = 0
        
        return dp[0]