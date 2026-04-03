from collections import defaultdict

class AirportRoutes:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addRoute(self, start, destination):
        self.graph[start].append(destination)

    def printRoutes(self, start, destination):
        all_paths = []
        curr_path = [start]
        curr_path_set = set([start])
        
        self.printRoutesDFS(start, destination, curr_path, curr_path_set, all_paths)

        print(all_paths)

    def printRoutesDFS(self, start, destination, curr_path, curr_path_set, all_paths):
        if start == destination:
            all_paths.append(curr_path.copy())
            return
        
        for nei in self.graph[start]:
            if nei not in curr_path_set:
                curr_path.append(nei)
                curr_path_set.add(nei)

                self.printRoutesDFS(nei, destination, curr_path, all_paths)

                curr_path.pop()
                curr_path_set.remove(nei)

