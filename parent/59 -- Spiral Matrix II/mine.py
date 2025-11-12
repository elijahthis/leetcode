class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Fastest
        matrix = [[0]*n for _ in range(n)]
        hashM = {
            (1,0):(0,1),
            (0,1):(-1,0),
            (-1,0):(0,-1),
            (0,-1):(1,0),
        }

        def outOfBounds(r,c):
            return (not 0 <= r < n) or (not 0 <= c < n) or matrix[r][c]
        
        def dfs(r,c, h,v):
            if outOfBounds(r,c) and outOfBounds(r+h,c+v):
                return
            
            
            if outOfBounds(r+v,c+h):
                matrix[r][c] = matrix[r-v][c-h] + 1
                nh, nv = hashM[(h,v)]
                dfs(r+nv, c+nh, nh, nv)
            else:
                matrix[r][c] = matrix[r-v][c-h] + 1
                dfs(r+v, c+h, h, v)
            
        
        dfs(0,0,1,0)
        return matrix