from typing import List, Optional

class Solution:
    # CORRECT, but kinda slow. It's accepted sha
    # O(m*n) time complexity
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroCoordinates = []
        # [(1,2), (2,4)]
        rowZero = False

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r == 0:
                       rowZero = True
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0