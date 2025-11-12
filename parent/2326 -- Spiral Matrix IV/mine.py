# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        r,c = 0,0
        matrix[r][c] = head.val


        def isWithinBounds(r,c):
            return 0 <= r < m and 0 <= c < n and matrix[r][c] == -1
        
        while head:
            for i in range(4):
                dr, dc = directions[i]
                while head.next and isWithinBounds(r+dr,c+dc):
                    head = head.next
                    r, c = r+dr, c+dc
                    matrix[r][c] = head.val
            if not head.next:
                head = None

        return matrix