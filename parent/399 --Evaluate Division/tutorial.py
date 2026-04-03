from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list) # a -> [b, a/b]
        
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1/values[i]])


        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1

            q, visited = deque(), set()
            q.append([start, 1])
            visited.add(start)
            
            while q:
                n, w = q.popleft()

                if n == end:
                    return w
                
                for nei, wei in graph[n]:
                    if nei not in visited:
                        q.append([nei, w*wei])
                        visited.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
