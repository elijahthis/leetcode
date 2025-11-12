class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Basially 3Sum with an extra for loop
        # Time: O(n^3)
        # Space: O(1)
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                l, r  = j+1, len(nums)-1

                while l < r:
                    fourSum = nums[i] + nums[j] + nums[l] + nums[r]

                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        # check for l AND r duplicates
                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        while nums[r] == nums[r+1] and l < r:
                            r -= 1
        return res