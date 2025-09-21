from typing import List 

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        delta = (sum_alice - sum_bob) // 2

        alice_hash = set(aliceSizes)

        for num in bobSizes:
            if num+delta in alice_hash:
                return [num+delta, num]