class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Most optimal for both time and space

        # Time Complexity: O(m × n)
        # Space Complexity: O(1)

        rows, cols = len(matrix), len(matrix[0])
        
        for r in range(rows):
            if r > 0:
                for c in range(1, cols):
                    if matrix[r][c] != matrix[r-1][c-1]:
                        return False
        
        return True

