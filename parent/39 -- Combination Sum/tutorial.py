class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(2ⁿ) worst case. Pruning improves this

        result = []

        def backtrack(i: int, curr: List[int], currSum: int):
            # base case: sum == target
            if currSum == target:
                result.append(curr.copy())
                return
            
            # end early if it's not possible. Pruning
            if i >= len(candidates) or currSum > target:
                return
            
            # We have two choices at every step:
            # 1. Include the current candidate
            # 2. Skip the current candidate
            # This is to avoid repetition
            curr.append(candidates[i])
            backtrack(i, curr, currSum+candidates[i])
            curr.pop()

            backtrack(i+1, curr, currSum)
        
        backtrack(0, [], 0)
        return result