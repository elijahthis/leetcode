class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Pure Recursion (DFS) + minmax (no memoization)
        # Slightly inefficient, but passes Leetcode (beats 5%)
        # Time: O(2^n)
        # Space: O(n)
        
        n = len(nums)
        total = sum(nums)

        def dfs(l,r):
            if l == r:
                return nums[l]
            if l > r:
                return 0
            
            return max(min(nums[l] + dfs(l+2, r), nums[l] + dfs(l+1, r-1)), min(nums[r] + dfs(l, r-2), nums[r] + dfs(l+1, r-1)))

        return (total - dfs(0, n-1)) <= (total / 2)