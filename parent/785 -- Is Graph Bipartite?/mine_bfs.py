from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Time: O(V+E). Each node is visited once. Each edge is processed once in adjacency list. Beats 100%
        # Space: O(V)

        visited = {}    #node->0,1
        
        def bfs(start, color):
            q = deque()
            q.append(start)
            visited[start] = color
            
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if nei in visited:
                        if visited[nei] == visited[curr]:
                            return False
                    else:
                        visited[nei] = (visited[curr]+1)%2
                        q.append(nei)
            return True
        
        for i in range(len(graph)):
            if i not in visited:
                if not bfs(i, 0):
                    return False

        return True