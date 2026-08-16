class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Fastest and most efficient
        # Time:  O(m + n)
        # Space: O(1)
        
        rows = len(matrix)
        r, c  = 0, len(matrix[0])-1

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        
        return False