class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Binary search problem
        # Time Complexity: O(n log(max(nums)))
        # Space Complexity: O(1) -- constant space

        def is_valid(capability: int) -> bool:
            count = 0
            i = 0

            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2
                else:
                    i += 1
            
            return count >= k

        result = 0
        l,r = min(nums), max(nums)

        while l<=r:
            mid = (l+r)//2
            
            if is_valid(mid):
                result = mid
                r = mid-1

            else:
                l = mid+1
            
        return result

""" 
What’s the right approach?

For this problem, the binary search + greedy method works much better:

Guess a maximum capability x.

Greedily try to rob houses without exceeding x.

If you can rob at least k houses, x is feasible.

Binary search on x gives the minimum feasible capability.

Time complexity: O(n log(max(nums))).
Space complexity: O(1).

"""  