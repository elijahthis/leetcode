class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Fastest
        # Time: O(M×N)
        # Space: O(M×N)

        m, n = len(matrix), len(matrix[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = []

        dirInd = 0
        visited = set()
        x,y = 0,0

        def isWithinBounds(x, y):
            return 0 <= x < m and 0 <= y < n and (x,y) not in visited

        while isWithinBounds(x,y):
            res.append(matrix[x][y])
            visited.add((x,y))

            new_x = x + directions[dirInd][0]
            new_y = y + directions[dirInd][1]

            if not isWithinBounds(new_x, new_y):
                # change direction
                dirInd = (dirInd + 1) % 4
                new_x = x + directions[dirInd][0]
                new_y = y + directions[dirInd][1]
            
            x, y = new_x, new_y
        
        return res