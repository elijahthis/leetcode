class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Uses DFS + backtracking.
        # The .copy() ensures each stored path is independent.
        # The recursion explores every possible path from source to target.

        # Time: O(P × L)    P = number of paths from source to target, L = average path length (up to N)
        # Space: O(P × L + N)

        res = []
        n = len(graph)

        def dfs(i: int, path: List[int]):
            if i == n-1:
                res.append(path.copy())
                return
            
            for neigh in graph[i]:
                path.append(neigh)
                dfs(neigh, path)
                path.pop()
            
        dfs(0, [0])
        return res
        

        