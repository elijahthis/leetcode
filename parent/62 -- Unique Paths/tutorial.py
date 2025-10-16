class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(mn)
        # Space: O(n)
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            
            row = newRow[::]
        
        return row[0]



    # same thing
    # def uniquePaths(self, m: int, n: int) -> int:
    #     res = [1] * n

    #     for irow in range(m-1):
    #         for icol in range(n-1):
    #             res[n-2-icol] = res[n-2-icol] + res[n-1-icol]
        
    #     print(res)
    #     return res[0]