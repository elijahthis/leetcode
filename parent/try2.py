def smallestDiff(arr):
    arr.sort()
    diff = abs(arr[1] - arr[0])
    res = [arr[0], arr[1]]

    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i-1]) < diff:
            res = [arr[i-1], arr[i]]
    
    return res


arr = [24, 12, 34, 64, 81, 47, 32]
print(smallestDiff(arr))