class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Too Fragile / Complicated / Britle
        # Time:  O(log(min(m,n)))
        # Space: O(n)
        
        if not nums1 and not nums2:
            return 0
            
        larger, smaller = nums1, nums2
        if len(nums1) < len(nums2):
            larger, smaller = smaller, larger
        
        m, n = len(larger), len(smaller)
        halfLen = (m+n) // 2

        l, r = 0, (n-1)
        bigR = halfLen-1
        
        while l <= r:
            mid = (l + r) // 2
            bigR = halfLen - mid - 2
            
            if mid < n-1 and bigR >= 0 and larger[bigR] > smaller[mid+1]:
                l = mid+1
            elif smaller[mid] > larger[bigR+1]:
                r = mid-1
            else:
                break
            
            if l >= n:
                bigR = halfLen - n - 1
                break
            elif r < 0:
                bigR = halfLen-1
                break
                
        
        res = 0
        mid = halfLen - bigR - 2

        border_val = larger[0]
        if bigR < 0 and smaller:
            border_val = smaller[mid]
        elif mid < 0:
            border_val = larger[bigR]
        else:
            border_val = max(larger[bigR], smaller[mid])

        next_val = larger[0]
        
        if bigR < m-1:
            next_val = larger[bigR+1]
            
            if halfLen - bigR - 2 < n-1:
                next_val = min(next_val, smaller[halfLen - bigR - 1])
        else:
            next_val = smaller[0]
        
        return float(next_val) if (m+n)%2 == 1 else float(border_val + next_val) / 2

