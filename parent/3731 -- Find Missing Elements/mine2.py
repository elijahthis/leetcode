class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        boolArr = [0] * 100
        minim, maxim = 100,0
        for num in nums:
            boolArr[num-1] = 1
            minim = min(num, minim)
            maxim = max(num, maxim)
        
        return [x for x in range(minim, maxim+1) if not boolArr[x-1]]