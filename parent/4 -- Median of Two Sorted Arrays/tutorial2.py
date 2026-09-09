class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Enforce nums1 as the smaller array to guarantee O(log(min(m, n)))
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
            
        m, n = len(A), len(B)
        
        # Binary search bounds
        l, r = 0, m
        
        # (m + n + 1) // 2 ensures that if total length is odd, 
        # the left partition will hold exactly one more element than the right.
        half_len = (m + n + 1) // 2
        
        while l <= r:
            i = (l + r) // 2      # Partition index for A
            j = half_len - i      # Partition index for B
            
            # Fetch values immediately to the left and right of the partition
            # Use -infinity / infinity if the partition is at the array's boundary
            A_left = A[i-1] if i > 0 else float('-inf')
            A_right = A[i] if i < m else float('inf')
            
            B_left = B[j-1] if j > 0 else float('-inf')
            B_right = B[j] if j < n else float('inf')
            
            # Check if we have found a valid partition
            if A_left <= B_right and B_left <= A_right:
                
                # If total length is odd, the median is just the max of the left side
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                
                # If total length is even, we average the max of left and min of right
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            # If A's left side is too big, move the partition left
            elif A_left > B_right:
                r = i - 1
            # If A's right side is too small, move the partition right
            else:
                l = i + 1