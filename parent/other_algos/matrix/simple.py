from typing import List

def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A)
    res = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
    
    return res

print(multiply([[1,2,3,4],[2,2,4,2],[4,1,5,7], [4,1,5,7]], [[1,2,5,3],[5,3,2,7],[2,2,4,3],[1,2,5,3]]))