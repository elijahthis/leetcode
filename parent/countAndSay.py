# 1 - "1"
# 2 - "11"
# 3 - "21"
# 4 - "1211"
# 5 - "111221"
# 6 - "312211"

def countAndSay(n: int):
    if n == 1:
        return '1'

    res = []

    count = 1
    prev = countAndSay(n-1)

    for i in range(1, len(prev)):
        if prev[i] == prev[i-1]:
            count += 1
        else:
            res.append(str(count) + prev[i-1])
            count = 1

    res.append(str(count) + prev[-1])
    return "".join((res))

print(countAndSay(6))
            
