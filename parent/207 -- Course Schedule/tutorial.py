class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The task reduces to detecting whether there’s a cycle in this graph.
        # If there’s a cycle → not possible to complete all courses.
        # If acyclic → possible to complete all courses.
        # Time: O(V + E)
        # Space: O(V + E)

        visited = set()

        # Build adjacency list
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs: int):
            if crs in visited:
                return False        # cycle detected
            
            if preMap[crs] == []:
                return True         # no prerequisites or already validated

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visited.remove(crs)
            preMap[crs] = []        # mark as fully processed (memoization)
            return True


        # Run DFS on all nodes
        # Ensures disconnected components (separate course groups) are all checked.
        for crs in range(numCourses):
            if not dfs(crs):  
                return False  
        return True