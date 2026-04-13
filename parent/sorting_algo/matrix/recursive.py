def add(A, B):
    m, n = len(A), len(A[0])
    res = [[0]*n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            res[r][c] = A[r][c] + B[r][c]
    return res

def recursive_multiply(A,B):
    n = len(A)
    res = [[0]*n for _ in range(n)]

    if n <= 2:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += A[i][k] * B[k][j]
    else:
        # A11.B11 + A12.B21  
        tl = add(recursive_multiply([r[:n//2] for r in A[:n//2]], [r[:n//2] for r in B[:n//2]]), 
                 recursive_multiply([r[n//2:] for r in A[:n//2]], [r[:n//2] for r in B[n//2:]]))
        

        # A11.B12 + A12.B22
        tr =  add(recursive_multiply([r[:n//2] for r in A[:n//2]], [r[n//2:] for r in B[:n//2]]),
                  recursive_multiply([r[n//2:] for r in A[:n//2]], [r[n//2:] for r in B[n//2:]]))
           
        # A21.B11 + A22.B21
        bl = add(recursive_multiply([r[:n//2] for r in A[n//2:]], [r[:n//2] for r in B[:n//2]]),
                 recursive_multiply([r[n//2:] for r in A[n//2:]], [r[:n//2] for r in B[n//2:]]))
         
        # A21.B12
        # A22.B22
        br = add(recursive_multiply([r[:n//2] for r in A[n//2:]], [r[n//2:] for r in B[:n//2]]),
                 recursive_multiply([r[n//2:] for r in A[n//2:]], [r[n//2:] for r in B[n//2:]]))

        print(tl)
        for r in range(n//2):
            for c in range(n//2):
                res[r][c] = tl[r][c]
            for c in range(n//2,n):
                res[r][c] = tr[r][c-(n//2)]
        for r in range(n//2,n):
            for c in range(n//2):
                res[r][c] = bl[r-(n//2)][c]
            for c in range(n//2,n):
                res[r][c] = br[r-(n//2)][c-(n//2)]

    return res

print(recursive_multiply([[1,2,3,4],[2,2,4,2],[4,1,5,7], [4,1,5,7]], [[1,2,5,3],[5,3,2,7],[2,2,4,3],[1,2,5,3]]))
# print(add([[1,2]], [[2,4]]))