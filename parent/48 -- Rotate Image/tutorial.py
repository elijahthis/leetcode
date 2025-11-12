class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time: O(n²) -- Each element is moved once
        #Space: O(1) -- No extra space
        l,r = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):    # cos we want len-1 iterations
                top, bottom = l, r  # initialize at l,r
                
                # save the top left value
                topLeft = matrix[top][l+i]

                # swap in reverse
                matrix[top][l+i] = matrix[bottom-i][l]       # move bl into tl
           
                matrix[bottom-i][l] = matrix[bottom][r-i]    # move br into bl
                matrix[bottom][r-i] = matrix[top+i][r]       # move bl into tl
                matrix[top+i][r] = topLeft     # move bl into tl

            l += 1
            r -= 1
