def removeDuplicates(nums: List[int]) -> int:
    l = 0
    for n in nums:
        if l < 2 or n != nums[l - 2]:
            nums[l] = n
            l += 1
    return l
