def wiggle_sort(self, nums: List[int]):
        # sort, then swap adjacent elements if they don't meet the condition
        # Time: O(nlogn)
        nums.sort()
        
        for i in range(1, len(nums)):
            if i%2 == 0 and nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]