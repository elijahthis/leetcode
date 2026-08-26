class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Too Fragile / Complicated
        # Time:  O(log(min(m,n)))
        # Space: O(n)
        
        A, B = nums1, nums2     # A is the shorter array
        total_len = len(A) + len(B)
        half_len = (total_len+1) // 2

        if len(A) > len(B):
            A, B = B, A

        # run binary search on A (shorter array)
        l, r = 0, len(A)-1
        while True:
            i = (l+r) // 2            # Partition index for A
            j = half_len - i - 2      # Partition index for B

            A_Left = A[i] if i >= 0 else float('-inf'),
            A_Right = A[i+1] if (i+1) < len(A) else float('inf')
            B_Left = B[j] if j >= 0 else float('-inf'), 
            B_Right = B[j+1] if (j+1) < len(B) else float('inf')

            # Check if we have found a valid partition
            if A_Left <= B_Right and B_Left <= A_Right:
                if total_len%2 == 1:
                    return min(A_Right, B_Right)                                # odd length
                return float(max(A_Left, B_Left) + min(A_Right, B_Right)) / 2   # even length
            elif A_Left > B_Right:
                r = i-1
            else:
                l = i+1

