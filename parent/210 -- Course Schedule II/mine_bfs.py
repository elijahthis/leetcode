from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time: O(V + E)
        # Space: O(V + E)

        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph and indegree count
        for crs, pre in prerequisites:
            graph[pre].append(crs)  # pre → crs
            indegree[crs] += 1

        # Initialize queue with courses having no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for neigh in graph[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        # If all courses are taken, return order, else empty list (cycle detected)
        return order if len(order) == numCourses else []
