class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DFS + Memoization
        # Time: O(amount * n)
        # Space: O(amount * n)

        res = 0
        memo = {}

        def dfs(a,i):
            if (a,i) in memo:
                return memo[(a,i)]

            if a == amount:
                memo[(a,i)] = 1
                return 1

            if a > amount or i == len(coins):
                memo[(a,i)] = 0
                return 0
            
            # Choice 1: Take the current coin (stay on index i)
            # Choice 2: Skip the current coin (move to index i + 1)
            memo[(a,i)] = dfs(a+coins[i], i) + dfs(a, i+1)
            return memo[(a,i)]

        return dfs(0, 0)
            