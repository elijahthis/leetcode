class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sorting + two pointers pattern
        # Greedy
        # Time: O(nlogn+mlogm)
        # Space: O(1) aux.
        # Same as #2410

        g.sort()
        s.sort()

        i = j = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i
            