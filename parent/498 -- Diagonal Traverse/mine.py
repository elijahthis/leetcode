class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Time: O(m × n) — each element is visited exactly once.
        # Space: O(1)

        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        r,c = 0,0
        di = 1
        res = []

        while len(res) < rows*cols:
            res.append(mat[r][c])
            
            nr, nc = r-di, c+di

            # boundary conditions
            if nr < 0 or nr == rows or nc < 0 or nc == cols:
                if di == 1:         # if moving up-right
                    if c+1 < cols:
                        c += 1      # shift right
                    else:
                        r += 1      # shift down
                else:               # if moving down-left
                    if r+1 < rows:
                        r += 1      # shift down
                    else:
                        c += 1      # shift right
                
                di *= -1            # change direction
            else:
                r,c = nr, nc

        return res
