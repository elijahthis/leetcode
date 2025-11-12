class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.m, self.n, self.tree = m, n, [[0] * (2*n) for _ in range(2*m)]
        
        for i in range(m):
            self.tree[i+m][n:] = matrix[i]
        for i in range(2*m-2, -1, -1):
            for j in range(n, 2*n):
                self.tree[i//2][j] = self.tree[i][j] + self.tree[i+1][j]
        for i in range(2*m):
            for j in range(2*n-2, -1, -1):
                self.tree[i][j//2] = self.tree[i][j] + self.tree[i][j+1]

    def update(self, row: int, col: int, val: int) -> None:
        row += self.m
        col += self.n
        diff = val - self.tree[row][col]
        while row > 0:
            curCol = col
            while curCol > 0:
                self.tree[row][curCol] += diff
                curCol //= 2
            row //= 2

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def pick(l: int, r: int) -> List[int]:
            candidates = []
            while l <= r:
                if l % 2:
                    candidates.append(l)
                    l = (l+1)//2
                else:
                    l //= 2
                if not r % 2:
                    candidates.append(r)
                    r = (r-1)//2
                else:
                    r //= 2
            return candidates

        rSum = 0
        for row in pick(row1 + self.m, row2 + self.m):
            for col in pick(col1 + self.n, col2 + self.n):
                rSum += self.tree[row][col]
        return rSum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)