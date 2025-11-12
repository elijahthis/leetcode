class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Time: O(n^(k)−1)  i.e O(n^3)
        # Space: O(k) + O(m)

        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i-1] == nums[i]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            else:
                l, r = start, len(nums) - 1
                while l < r:
                    twoSum = nums[l] + nums[r]
                    if twoSum < target:
                        l += 1
                    elif twoSum > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])

                        l += 1
                        r -= 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                        while nums[r] == nums[r+1] and l < r:
                            r -= 1
                        
        
        kSum(4, 0, target)
        return res