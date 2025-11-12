from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        
        diagonals = defaultdict(list)
        res = []

        for r in range(len(nums)):
            for c in range(len(nums[r])):
                diagonals[r+c].append(nums[r][c])
            

        for k in sorted(diagonals.keys()):
            res.extend(reversed(diagonals[k]))

        return res