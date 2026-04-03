class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time: O(m+n). Very fast
        # Space: O(1)
        
        i = m-1
        j = n-1

        while j >= 0:
            if i < 0 or nums2[j] > nums1[i]:
                nums1[i+j+1] = nums2[j]
                j -= 1
            else:
                nums1[i+j+1] = nums1[i]
                i -= 1