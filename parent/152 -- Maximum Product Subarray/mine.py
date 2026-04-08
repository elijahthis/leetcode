class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # The solution is correct, but this is hard to verify due to its complexity
        # Time: O(n)
        # Space: O(n)
        res = nums[0]
        dp = [nums[0]] * len(nums)
        min_neg = min(0, nums[0])

        for i in range(1, len(nums)):
            prev, curr = dp[i-1], nums[i]
            if prev > 0:
                if curr >= 0:
                    dp[i] = prev * curr
                    min_neg *= curr
                else:
                    if min_neg < 0:
                        dp[i] = curr * min_neg
                    else:
                        dp[i] = curr
                    
                    min_neg = curr*prev if prev > 0 else curr
    
            else:
                if curr >= 0:
                    dp[i] = curr
                    min_neg *= curr
                else:
                    if min_neg < 0:
                        dp[i] = max(curr * min_neg, prev * curr)
                    else:
                        dp[i] = prev * curr
                    min_neg = curr*prev if prev > 0 else curr
            res = max(res, dp[i])

        return res