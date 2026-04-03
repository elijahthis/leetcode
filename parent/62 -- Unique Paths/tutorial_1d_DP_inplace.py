class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(m × n)
        # Space: O(n)
        
        arr = [1] * n

        for _ in range(m-1):
            for c in range(1, n):
                arr[c] += arr[c-1]

        return arr[-1]
    

    # 1 3 6 10 15 21 28
    # 1 2 3 4  5  6  7 
    # 0 1 1 1  1  1  1  