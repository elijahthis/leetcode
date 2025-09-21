class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ANALYSIS:
        # - We can use a hash map to keep track of the indexes of numbers
        # - We can iterate through the numbers and check if the complement is in the hash map
        # - If the complement is in the hash map, then we can return the indexes
        # - The time complexity is O(n) where n is the number of numbers
        # - The space complexity is O(n) where n is the number of numbers because we are using hash maps
        prevHash = {} # num -> index

        for i, n in enumerate(nums):
            rem = target - n
            if rem in prevHash:
                return [prevHash[rem], i]

            prevHash[n] = i