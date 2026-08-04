class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Optimal Top-Down DP (Memoization)
        # More time efficient, cos memo
        # Time: O(n^2)
        # Space: O(n^2)

        n = len(nums)
        total = sum(nums)
        memo = {}

        def dfs(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            
            # early returns
            if l == r:
                return nums[l]
            if l > r:
                return 0

            # minmax
            memo[(l,r)] = max(min(nums[l] + dfs(l+2, r), nums[l] + dfs(l+1, r-1)), min(nums[r] + dfs(l, r-2), nums[r] + dfs(l+1, r-1)))
            return memo[(l,r)]

        return (total - dfs(0, n-1)) <= (total / 2)