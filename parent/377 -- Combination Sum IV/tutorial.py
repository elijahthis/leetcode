from typing import List

class Solution:
    # Dynamic programming
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp: dict[int, int] = {0: 1}

        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
               dp[total] += dp.get(total - n, 0)
    
        return dp[target]

soln = Solution()
print(soln.combinationSum4([1,2,3], 4))


"""
Example Walkthrough

Let’s go through a concrete example:

Suppose nums = [1, 2, 3] and target = 4.

    We initialize dp = {0: 1}.
    We start iterating over total from 1 to 4.

For total = 1:

    dp[1] = 0
    For n = 1: dp[1] += dp[0] → dp[1] = 1 (using 1)
    For n = 2: dp[1] += dp[-1] → no change (sum cannot be negative)
    For n = 3: dp[1] += dp[-2] → no change

Result after this iteration: dp = {0: 1, 1: 1}

For total = 2:

    dp[2] = 0
    For n = 1: dp[2] += dp[1] → dp[2] = 1 (using 1, 1)
    For n = 2: dp[2] += dp[0] → dp[2] = 2 (using 2)
    For n = 3: dp[2] += dp[-1] → no change

Result after this iteration: dp = {0: 1, 1: 1, 2: 2}

For total = 3:

    dp[3] = 0
    For n = 1: dp[3] += dp[2] → dp[3] = 2 (using 1,1,1 or 1,2)
    For n = 2: dp[3] += dp[1] → dp[3] = 3 (using 2,1)
    For n = 3: dp[3] += dp[0] → dp[3] = 4 (using 3)

Result after this iteration: dp = {0: 1, 1: 1, 2: 2, 3: 4}

For total = 4:

    dp[4] = 0
    For n = 1: dp[4] += dp[3] → dp[4] = 4 (using 1,1,1,1 or 1,1,2 or 1,3)
    For n = 2: dp[4] += dp[2] → dp[4] = 6 (using 2,2 or 2,1,1)
    For n = 3: dp[4] += dp[1] → dp[4] = 7 (using 3,1)

Final result: dp = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}

Thus, there are 7 ways to form the target sum 4 using the numbers [1, 2, 3].
"""