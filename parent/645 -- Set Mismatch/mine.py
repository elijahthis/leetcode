class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n). Need bit manipulation use less space

        seen = set()
        complete = incomplete = 0
        dupl = 0

        for i in range(len(nums)):
            if nums[i] in seen:
                dupl = nums[i]
            seen.add(nums[i])
            complete += i+1
            incomplete += nums[i]

        return [dupl, dupl+complete-incomplete]
            