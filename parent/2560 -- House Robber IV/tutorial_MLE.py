class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # NOT good enough -- this solution gives Memory Limit Exceeded
        # max house among robbed
        # try to maximize it
        # rob at least k

        # brute fore is 2^n
        # DP brings it down to n^2
        # this is top-down solution

        cache = {}
        def backtrack(i,k):
            # base cases
            if i >= len(nums):
                if k:
                    return float('inf') # not enough houses robbed
                return 0 # robbed enough houses, capability is 0
            if (i,k) in cache:
                return cache[(i,k)]
            
            # Recursive choices
            res1 = max(nums[i], backtrack(i+2, k-1))
            res2 = backtrack(i+1, k)

            res = min(res1, res2)

            cache[(i,k)] = res
            return res

        return backtrack(0, k)