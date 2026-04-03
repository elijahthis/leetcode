from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        # meh. slower than my two
        # bucket sort
        counts = {}
        buckets = defaultdict(list)
        res = []

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        
        for key, val in counts.items():
            buckets[val].append(key)

        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c*i)
        
        return "".join(res)