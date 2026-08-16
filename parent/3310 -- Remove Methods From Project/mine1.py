from collections import defaultdict

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Time: O(n+m)
        # Space: O(n+m)
        
        adj_list = defaultdict(list)
        for node, nei in invocations:
            adj_list[node].append(nei)
        
        infected = set()
        visited = set()

        def dfs_infect(node):
            infected.add(node)

            for nei in adj_list[node]:
                if nei not in infected:
                    dfs_infect(nei)
        
        
        def dfs(node):
            if node in infected:
                return True
            
            visited.add(node)
            for nei in adj_list[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True
            
            return False
            
        dfs_infect(k)
        for i in range(n):
            if i not in infected:
                if dfs(i):
                    return list(range(n))
        
        return [x for x in range(n) if x not in infected]