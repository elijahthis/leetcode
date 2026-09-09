class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Time: O(n)
        # Space: O(1)

        # (first true condition): all elements are even - (only way for even parity) 
        allEven = True
        for num in nums1:
            if num%2 == 1:
                allEven = False
                break
        if allEven:
            return True
        
        # (second true condition): mix of even and odd or all odd, AND the smallest element is odd - (only way for odd parity) 
        if min(nums1) % 2 == 1:
            return True
        
        return False