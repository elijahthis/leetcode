class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # ✅ Optimal Solution (Boyer–Moore Voting Algorithm)
        # Time: O(n)
        # Space: O(1)
        # Because the majority element appears more than all others combined, 
        # it will always survive as the final candidate.
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

# nums = [2, 2, 1, 1, 1, 2, 2]
