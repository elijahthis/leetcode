class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0,0)
        digitLength = len(digits)
        for i in range(digitLength):
            digit = digits[digitLength-i-1] + 1 if i==0 else digits[digitLength-i-1]
            digits[digitLength-i-1] = digit % 10
            digits[digitLength-i-2] += digit // 10
        
        return digits[1:] if digits[0] == 0 else digits
            