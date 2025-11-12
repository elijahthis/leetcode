class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # You keep track of direction via (h, v) — horizontal and vertical components.
        # You maintain a step count that increases after every two turns.
        # A stepSet is used to determine when to increase the number of steps taken in each direction.
        # You collect valid coordinates in res and stop once len(res) == rows * cols.

        res = []
        self.step = 1
        stepSet = set([1])
        dirMap = {
            (1,0): (0,1),
            (0,1): (-1,0),
            (-1,0): (0,-1),
            (0,-1): (1,0)
        }

        # is

        def dfs(r,c, h,v, s):
            # use length of res to know it's complete
            if len(res) == (rows*cols):
                return
            
            if r in range(rows) and c in range(cols):
                res.append([r,c])

            if not s:
                # change direction
                h,v = dirMap[(h,v)]
                # use set to go the same no of steps twice, before incrementing
                if self.step in stepSet:
                    s = self.step
                    stepSet.remove(self.step)
                else:
                    s = self.step+1
                    stepSet.add(self.step+1)
                    self.step += 1

            dfs(r+v, c+h, h, v, s-1)

        dfs(rStart, cStart, 1, 0, self.step)
        return res

        