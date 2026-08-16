class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Best for interviews
        # Time: O(logmn)
        # Space: O(1)
        rows, cols = len(matrix), len(matrix[0])
        l, r =  0, (rows*cols) - 1

        while l <= r:
            mid = (l+r) // 2
            i, j = mid // cols, mid % cols
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid+1
            else:
                r = mid-1
        
        return False