def quick_sort(nums, left, right):
    if left >= right:
        return

    pivot = left
    i = left-1
    j = right+1

    while True:
        i += 1
        while nums[i] < nums[pivot]:
            i += 1
        
        j -= 1
        while nums[j] > nums[pivot]:
            j -= 1
        
        if i >= j:
            break
        
        nums[i], nums[j] = nums[j], nums[i]
    
    quick_sort(nums, left, j)
    quick_sort(nums, j+1, right)


nums = [9, 5, 2, 3, 4, 1, 4]
quick_sort(nums, 0, len(nums)-1)

print(nums)
