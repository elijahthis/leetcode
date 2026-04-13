class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n). Optimal, but slightly state-heavy
        # Space: O(n)
        
        res = 0
        start = end = 0
        nums_set = set(nums)
        visited = set()

        for num in nums_set:
            if num not in visited:
                visited.add(num)
                start = end = num

                while start-1 in nums_set:
                    start -= 1
                    visited.add(start)
                while end+1 in nums_set:
                    end += 1
                    visited.add(end)
                
                res = max(res, (end-start+1))
                
        
        return res
