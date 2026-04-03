class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Time: O(M*N)
        # Space: O(M*N)
        # Best time and space
        
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        val = 1

        while left <= right and top <= bottom:
            for y in range(left, right+1):
                print(top, y)
                res[top][y] = val
                val += 1
            top += 1

            for x in range(top, bottom+1):
                res[x][right] = val
                val += 1
            right -= 1

            if left <= right:
                for y in range(right, left-1, -1):
                    res[bottom][y] = val
                    val += 1
                bottom -= 1
            
            if top <= bottom:
                for x in range(bottom, top-1, -1):
                    res[x][left] = val
                    val += 1
                left += 1
        
        return res