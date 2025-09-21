from typing import List, Optional

class Solution:
    # CORRECT, but kinda slow. It's accepted sha
    # O(m*n) time complexity
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroCoordinates = []    # [(1,2), (2,4)]

        for r in range(len(matrix)):
            for i in range(len(matrix[r])):
                if matrix[r][i] == 0:
                   zeroCoordinates.append((r, i))
        
        for item in zeroCoordinates:
            matrix[item[0]] = [0] * len(matrix[item[0]])

            for r in range(len(matrix)):
                matrix[r][item[1]] = 0