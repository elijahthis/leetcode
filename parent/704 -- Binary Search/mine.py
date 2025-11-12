class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # time: O(logn)
        # space: O(1)
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
    
    # Steps:
    # 0, len(nums)-1
    # <=
    # r = mid-1
    # l = mid+1
