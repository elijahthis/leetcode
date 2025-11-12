class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count.get(num) > len(nums) / 2:
                return num