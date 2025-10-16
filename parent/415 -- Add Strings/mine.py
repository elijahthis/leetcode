class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        res = []

        carry = 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >=0:
                total += int(num1[i])
                i -= 1
            if j >= 0:
                total += int(num2[j])
                j -= 1
        
            res.append(str(total % 10))
            carry = total // 10
        
        return "".join(res[::-1])
            