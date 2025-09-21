class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ANALYSIS:
        # - sort the array
        # - iterate through the array
        # - for each element, use two pointers to find the other two elements
        # - if the sum is greater than 0, decrement the right pointer
        # - if the sum is less than 0, increment the left pointer
        # - if the sum is 0, add the triplet to the result
        # - skip duplicates
        # - return the result
        # - O(n^2) time complexity
        # - O(1) space complexity
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            # two-sum-ish solution
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    # update pointers
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return result