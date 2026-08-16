from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # More optimal for time and space
        # Time: O(n+m)
        # Space: O(n+m)
                
        adj_list = defaultdict(list)
        for node, nei in invocations:
            adj_list[node].append(nei)
        
        infected = set()

        def dfs_infect(node):
            infected.add(node)

            for nei in adj_list[node]:
                if nei not in infected:
                    dfs_infect(nei)
        
        dfs_infect(k)
        # Slight optimization: No need for second dfs
        # Just check if any uninfected node directly invokes an infected node
        for u,v in invocations:
            if u not in infected and v in infected:
                return list(range(n))
        
        return [x for x in range(n) if x not in infected]