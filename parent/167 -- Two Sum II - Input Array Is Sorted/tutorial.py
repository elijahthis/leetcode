class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ANALYSIS:
        # - two pointers
        # - if the sum is less than the target, increment the left pointer
        # - if the sum is greater than the target, decrement the right pointer
        # - if the sum is equal to the target, return the indices
        # - O(n) time complexity
        # - O(1) space complexity
        
        l, r = 0, len(numbers)-1

        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum < target:
                l += 1
            elif twoSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        
        return []
