class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m*n) time complexity
        # Space: O(m + n)
        rowSet = set()
        colSet = set()
        for irow in range(len(matrix)):
            for icol in range(len(matrix[irow])):
                if matrix[irow][icol] == 0:
                    rowSet.add(irow)
                    colSet.add(icol)
        
        for item in rowSet:
            matrix[item] = [0] * len(matrix[0])
        for item in colSet:
            for row in matrix:
                row[item] = 0