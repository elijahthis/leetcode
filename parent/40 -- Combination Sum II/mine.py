class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # using the logic of Combination Sum I
        # Time: O(2n)
        # Space: O(K×L+n)  -- (K = number of valid combinations, L = average combination length)
        candidates.sort()
        result = []

        def backtrack(i: int, curr: List[int], currSum: int):
            if currSum == target:
                result.append(curr.copy())
                return
            
            if i >= len(candidates) or currSum > target:
                return
            
            
            # Recursive Choices
            # 1. Include the current number
            curr.append(candidates[i])
            backtrack(i+1, curr, currSum+candidates[i])
            curr.pop()

            # 2. Skip the current number (and all its duplicates)
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i+1

            backtrack(i+1, curr, currSum)
        
        backtrack(0, [], 0)
        return result