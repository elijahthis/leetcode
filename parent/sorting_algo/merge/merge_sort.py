import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        return merge(left, right)
    
    return arr

def merge(left, right):
    i,j = 0,0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right  [j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    
    arr += left[i:]
    arr += right[j:]

    return arr

print(merge_sort([3, 1, 2]))
print(merge_sort([5, 4, 3, 2, 1]))
print(merge_sort([1, 2, 3, 4, 5]))

assert merge_sort([3, 1, 2]) == [1, 2, 3]
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert merge_sort(list(range(100))) == list(range(100))
assert merge_sort(list(range(100, 0, -1))) == list(range(1, 101))

arr = [random.randint(-1000, 1000) for _ in range(1000)]
assert merge_sort(arr) == sorted(arr)

# Empty list
assert merge_sort([]) == []
# Single element
assert merge_sort([1]) == [1]
# All elements the same
assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]