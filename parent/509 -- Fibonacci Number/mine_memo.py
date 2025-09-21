class Solution:
    def fib(self, n: int) -> int:
        # 0, 1, 1, 2, 3, 5, 8, 13, 21
        # memoization -- 2 vars
        # Time Complexity: O(n)
        # Space Complexity: O(1) -- Constant Time
        a,b = 0, 1
        for ind in range(n+1):
            if ind > 1:
                a,b = b, a+b
        
        return a if n==0 else b
    

    # def fib(self, n: int) -> int:
    #     # 0, 1, 1, 2, 3, 5, 8, 13, 21
    #     # memoization -- array
    #     # Time Complexity: O(n)
    #     # Space Complexity: O(n)
    #     memo = [0] * (n+1)
    #     for ind in range(n+1):
    #         if ind == 0 or ind == 1:
    #             memo[ind] = ind
    #         else:
    #             memo[ind] = memo[ind-1] + memo[ind-2]
        
    #     return memo[ind]
