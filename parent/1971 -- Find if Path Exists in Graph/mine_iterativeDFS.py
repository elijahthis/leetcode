import collections
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
        
        stack = []
        stack.append(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for item in graph[node]:
                    stack.append(item)


        return False
