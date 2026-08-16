class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # i prefer this
        # Time: O(n)
        # Space: O(n)

        hashN = set(nums)
        minim, maxim = min(nums), max(nums)
        res = []
        for i in range(minim, maxim):
            if i not in hashN:
                res.append(i)
        
        return res