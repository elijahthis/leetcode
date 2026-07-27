class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # allows for +ve and -ve numbers (not necessary for problem definition tho)

        max1 = max2 = float('-inf')
        min1 = float('inf')
        for num in nums:
            if num < min1:
                min1 = num
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

        return max((max1-1)*(max2-1), (max1-1)*(min1-1))