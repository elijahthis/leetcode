class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time: O(M*N)
        # Space: O(1)
        # Best time and space

        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1
        res = []

        while left <= right and top <= bottom:
            # left -> right
            for y in range(left, right+1):
                res.append(matrix[top][y])
            top += 1
            
            # top -> bottom
            for x in range(top, bottom+1):
                res.append(matrix[x][right])
            right -= 1

            # right -> left
            if top <= bottom:
                for y in range(right, left-1, -1):
                    res.append(matrix[bottom][y])
                bottom -= 1
            
            # bottom -> top
            if left <= right:
                for x in range(bottom, top-1, -1):
                    res.append(matrix[x][left])
                left += 1
        
        return res