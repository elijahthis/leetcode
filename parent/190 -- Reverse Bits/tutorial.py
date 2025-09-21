class Solution:
    def reverseBits(self, n: int) -> int:
        bin_form = bin(n)[2:]
        stringified_bits = (((32 - len(bin_form)) * '0') + str(bin_form))[::-1]

        return int(stringified_bits, 2)