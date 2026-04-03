# Lomuto Quick Sort
def quick_sort(arr, left, right):
    if left >= right:
        return

    # randomized pivot
    # pivotIndex = left + rand.Intn(right-left+1)
	# nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]

    pivot = right
    i = left-1

    for j in range(left, right):
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]

    quick_sort(arr, left, i-1)
    quick_sort(arr, i+1, right)

    # Optimization: Recurse on the smallest side first. Reduces worst-case stack depth from O(n) to O(logn)
    # if i-left < right-i:
    #     quick_sort(nums, left, i-1)
    #     quick_sort(nums, i+1, right)
    # else:
    #     quick_sort(nums, i+1, right)
    #     quick_sort(nums, left, i-1)


# nums = [2, 1, 8, 9, 7, 4]
nums = [1, 5, 2, 3, 4, 1, 4]
quick_sort(nums, 0, len(nums)-1)

print(nums)
