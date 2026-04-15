class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Greedy
        # Time: O(nlogn)
        # Space: O(n)

        diffs = sorted(capacity[i] - rocks[i] for i in range(len(rocks)))
        i = res = 0

        while i < len(diffs) and diffs[i] <= additionalRocks:
            if diffs[i] > 0:
                additionalRocks -= diffs[i]
            
            res += 1
            i += 1
        
        return res