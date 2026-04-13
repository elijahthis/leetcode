class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Union-Find (Disjoint Set Union)
        # Collapsing Union
        # Time: O(E⋅α(N))     α = inverse Ackermann (basically constant)
        # Space: O(N) 

        # Each node initially points to itself
        # This means every node starts as its own separate component
        parent = list(range(n))

        # FIND: returns the root (representative) of a node
        def find(x):
            # If x is not its own parent, it means it's not the root
            if parent[x] != x:
                # Path compression:
                # Recursively find the root and attach x directly to it
                # This flattens the tree for future queries (Collapsing Union)
                parent[x] = find(parent[x])
            return parent[x]

        # UNION: merge the sets containing u and v
        def union(u,v):
            parent[find(u)] = find(v)
        
        for u,v in edges:
            union(u,v)
        
        # Finally, check if source and destination share the same root
        return find(source) == find(destination)