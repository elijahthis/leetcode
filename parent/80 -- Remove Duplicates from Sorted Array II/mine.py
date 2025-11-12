class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # dupli → remembers the last number that was duplicated.
        # l → the position where the next valid element should go.
        # r → iterates through the array.
        dupli = float("inf")
        l = 0

        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            elif nums[r] != dupli:
                dupli = nums[r]
                l += 1
                nums[l] = nums[r]
        
        return l+1