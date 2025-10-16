class Solution:
    def intToRoman(self, num: int) -> str:
        # Map of values to their Roman numeral equivalents
        # Time Complexity: O(1) (bounded by the number of Roman numeral symbols, which is fixed).
        # Space Complexity: O(1) (result length is constant ≤ 15 characters).

        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        result = []
        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                result.append(syms[i])

        return "".join(result)
