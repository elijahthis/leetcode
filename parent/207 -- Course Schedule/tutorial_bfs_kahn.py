from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and indegree map
        adj = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        # Initialize queue with courses that have no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        finished = 0

        while q:
            curr = q.popleft()
            finished += 1  # This course can be completed
            
            # Decrease indegree of dependent courses
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # If we were able to process all courses → no cycle
        return finished == numCourses
