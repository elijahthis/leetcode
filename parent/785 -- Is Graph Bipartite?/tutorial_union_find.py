class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # same complexity, not very fast tho
        parent = list(range(len(graph)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u,v):
            parent[find(u)] = find(v)
        
        for u in range(len(graph)):
            for v in graph[u]:
                # If u and v are in same set → not bipartite
                if find(u) == find(v):
                    return False
                # Union all neighbors of u together
                # (group them as opposite of u)
                union(graph[u][0], v)

        return True