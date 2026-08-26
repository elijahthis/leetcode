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

    count = l = 0
    prev = countAndSay(n-1)

    while l < len(prev):
        while l < len(prev) and (l == 0 or prev[l] == prev[l-1]):
            count += 1
            l += 1
            continue

        res.append(str(count) + prev[l-1])
        if l < len(prev):
            count = 1
            l += 1

    if res[-1][-1] != prev[-1]:   
        res.append(str(count) + prev[l-1])
    return "".join((res))