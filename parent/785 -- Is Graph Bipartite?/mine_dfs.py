class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Time: O(V+E). Each node is visited once. Each edge is processed once in adjacency list. Beats 100%
        # Space: O(V)
        
        visited = {}    #node->0,1
        
        def dfs(node, color):
            if node in visited:
                return visited[node] == color
            
            visited[node] = color
            
            for nei in graph[node]:
                if not dfs(nei, (visited[node]+1)%2):
                    return False
                
            return True
        
        for i in range(len(graph)):
            if i not in visited:
                if not dfs(i, 0):
                    return False

        return True