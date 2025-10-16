import collections
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        q = collections.deque()

        # Step 1: Enqueue all border 'O's
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    q.append((r, c))
        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == 'O':
                    q.append((r, c))

        # Step 2: BFS from border 'O's to mark safe ones as 'S'
        while q:
            r, c = q.popleft()
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'S'
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    q.append((r + dr, c + dc))

        # Step 3: Flip all remaining 'O' to 'X' and 'S' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
