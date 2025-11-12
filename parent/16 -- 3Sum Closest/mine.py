class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        
        nums.sort()
        res = float('inf')
        # res = nums[0] + nums[1] + nums[2]     -- this initialization also works

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if abs(res-target) > abs(threeSum-target):
                    res = threeSum
                
                if threeSum == target:
                    return threeSum
                elif threeSum > target:
                    r -= 1
                else:
                    l += 1
                
        return res