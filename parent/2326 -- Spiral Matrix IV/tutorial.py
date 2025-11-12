class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        r, c, d = 0, 0, 0  # start direction: right

        while head:
            matrix[r][c] = head.val
            head = head.next
            if not head:
                break

            nr, nc = r + directions[d][0], c + directions[d][1]
            if not (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == -1):
                d = (d + 1) % 4
                nr, nc = r + directions[d][0], c + directions[d][1]
            r, c = nr, nc

        return matrix
