from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time: O(n + T)      -- > T = len(trust)
        # Space: O(T)

        heTrusts = defaultdict(set)     # citizen: [people he trusts]
        trustHim = defaultdict(set)     # citizen: [people he trusts]
        
        for tr in trust:
            heTrusts[tr[0]].add(tr[1])
            trustHim[tr[1]].add(tr[0])
        
        for person in range(1, n+1):
            if len(heTrusts[person]) == 0 and len(trustHim[person]) == n-1:
                return person

        return -1
