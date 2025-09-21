def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    result = 0
    total = nums[0]
    l, r = 0, 0

    while l <= r and r < len(nums):
        if total < target:
            print("ite 1")
            r += 1
            if r < len(nums):
                total += nums[r]
            continue
        else:
            print("ite 2")
            if result == 0:
                result = r-l+1
            else:
                result = min(result, r-l+1)
            total -= nums[l]
            l += 1
            continue
    
    return result
