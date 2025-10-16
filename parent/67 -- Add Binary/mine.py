class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time: O(max(len(a), len(b)))
        # Space: O(max(len(a), len(b)))
        
        if a == "0" and b == "0":
            return "0"
        
        maxLen = max(len(a), len(b))
        res = [0] * (maxLen + 1)
        hashM = {2: 0, 3: 1}

        for i in range(maxLen+1):
            left, right = 0, 0
            if i < len(a):
                left = a[len(a)-i-1]
            if i < len(b):
                right = b[len(b)-i-1]
            
            digit = int(left) + int(right)
            res[maxLen-i] += digit
            if res[maxLen-i] > 1:
                res[maxLen-i] = hashM[res[maxLen-i]]
                res[maxLen-i-1] += 1

        ptr = 0
        while res[ptr] == 0 and ptr < len(res):
            ptr += 1

        res = map(str, res[ptr:])
        
        return "".join(res)

