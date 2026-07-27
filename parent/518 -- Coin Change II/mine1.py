class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Correct, but TLE. Need to replace the loop
        # Time: O(amount * n²)
        # Space: O(amount * n)

        memo = {}

        def dfs(a,i):
            if (a,i) in memo:
                return memo[(a,i)]

            if a > amount:
                memo[(a,i)] = 0
                return 0
            if a == amount:
                memo[(a,i)] = 1
                return 1
            
            res = 0
            for j in range(i, len(coins)):
                res += dfs(a+coins[j], j)
            
            memo[(a,i)] = res
            return res

        return dfs(0, 0)
            