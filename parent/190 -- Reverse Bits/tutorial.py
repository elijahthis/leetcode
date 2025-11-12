class Solution:
    def reverseBits(self, n: int) -> int:
        # Converts the integer n into its binary string form (without the 0b prefix).
        bin_form = bin(n)[2:]

        # Pads the binary string to 32 bits with leading zeros.
        # [::-1] Reverses the binary string.
        stringified_bits = (((32 - len(bin_form)) * '0') + str(bin_form))[::-1]

        # Converts the reversed binary string back to an integer.
        return int(stringified_bits, 2)