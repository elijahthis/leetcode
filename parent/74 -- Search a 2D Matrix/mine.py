class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Fastest
        # Time: O(m⋅logn)
        # Space: O(1)
        for row in matrix:
            if row[-1] >= target:
                l,r = 0, len(row)-1
                while l <= r:
                    mid = (l + r) // 2

                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        r = mid-1
                    else:
                        l = mid+1
                return False
        
        return False