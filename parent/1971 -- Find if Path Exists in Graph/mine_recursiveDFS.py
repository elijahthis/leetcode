class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Time: O(N + E)
        # Space: O(N + E)
        # create graph
        graph = defaultdict(list)
        visited = set()

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)

            for item in graph[node]:
                if item not in visited:
                    if dfs(item):
                        return True
            
            return False


        return dfs(source)
