class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Time : O(m × n)
        # Space : O(m × n)
        # Optimal+Most intuitive

        res = [[-1 for _ in range(n)] for _ in range(m)]
        top, bottom = 0, m-1
        left, right = 0, n-1

        while head and top <= bottom and left <= right:
            for i in range(left, right+1):
                if not head:
                    break
                res[top][i] = head.val
                head = head.next
            top += 1
            
            for i in range(top, bottom+1):
                if not head:
                    break
                res[i][right] = head.val
                head = head.next
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    if not head:
                        break
                    res[bottom][i] = head.val
                    head = head.next
            bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    if not head:
                        break
                    res[i][left] = head.val
                    head = head.next
            left += 1

        return res