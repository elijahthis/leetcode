class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # same as neet's
        # Time: O(m*n*4^L)
        # Space: O(L)       L -> length of the word
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(r: int, c: int, i):
            # base case
            if i == len(word):
                return True
            
            # out of bounds
            # element doesn't match
            # already visited
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r,c) in visited):
                return False
            
            visited.add((r,c))
            res = backtrack(r, c-1, i+1) or backtrack(r, c+1, i+1) or backtrack(r-1, c, i+1) or backtrack(r+1, c, i+1)
            visited.remove((r,c))
            return res
        
           
        for r in range(len(board)):
            for c in range(len(board[r])):
                if backtrack(r, c, 0):
                    return True
        
        return False