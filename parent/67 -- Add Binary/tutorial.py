class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time: O(max(len(a), len(b)))
        # Space: O(max(len(a), len(b)))
        # EASIER to explain in an interview
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            res.append(str(total % 2))   # Add current bit
            carry = total // 2           # Update carry

        return "".join(reversed(res))
