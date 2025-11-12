class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        steps = 1
        r, c = rStart, cStart
        
        while len(res) < rows * cols:
            for i in range(4):
                dr, dc = directions[i]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                # Increase step size after moving horizontally or vertically twice
                if i % 2 == 1:
                    steps += 1
        return res
