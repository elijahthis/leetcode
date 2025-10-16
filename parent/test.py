def sortOrder(input, order):
    hashM = {}
    arr = []

    for char in input:
        hashM[char] = hashM.get(char,0) + 1

    for char in order:
        arr.append(char * hashM[char])
    
    return "".join(arr)

print(sortOrder("abcca", "cba"))