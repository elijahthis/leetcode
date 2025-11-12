class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Fastest
        res = []
        visited = set()
        M, N = len(matrix), len(matrix[0])
        hashM = {
            (1,0): (0,1),
            (0,1): (-1,0),
            (-1,0): (0,-1),
            (0,-1): (1,0)
        }

        def outOfBounds(r,c):
            return (not (0 <= r < M)) or (not (0 <= c < N)) or (r,c) in visited

        def dfs(r, c, h, v):
            if outOfBounds(r,c) and outOfBounds(r+v,c+h):
                return
            
            if outOfBounds(r+v,c+h):
                res.append(matrix[r][c])
                visited.add((r,c))

                nh,nv = hashM[(h,v)]
                dfs(r+nv,c+nh,nh,nv)
                pass
            else:
                res.append(matrix[r][c])
                visited.add((r,c))

                dfs(r+v,c+h,h,v)
        
        dfs(0,0,1,0)
        return res

