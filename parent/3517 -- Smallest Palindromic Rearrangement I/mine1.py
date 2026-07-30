import math

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Time: O(nlogn)
        # Space:  O(n)
        
        if len(s) < 4:
            return s
        
        n = len(s)
        arr = list(s)
        orders, res = [], []

        for i in range(math.floor(n/2)):
            orders.append(ord(arr[i]))
        orders.sort()

        for num in orders:
            res.append(chr(num))
        
        res = res[::] + ([] if n%2 == 0 else [s[math.floor(n/2)]]) + res[::-1]

        return ''.join(res)