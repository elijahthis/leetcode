from collections import defaultdict
class AirportRoutes:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def addRoute(self, start, destination):
        self.graph[start].add(destination)

    def printRoutes(self, start, destination):
        all_paths = []
        curr_path = [start]
        curr_path_set = set([start])

        self.printRoutes_dfs(start, destination, curr_path, all_paths, curr_path_set)
        
        print(all_paths)

    def printRoutes_dfs(self, start, destination, curr_path, all_paths, curr_path_set):
        if start == destination:
            all_paths.append(curr_path.copy())
            return
        
        for nei in self.graph[start]:
            if nei not in curr_path_set:
                curr_path.append(nei)
                curr_path_set.add(nei)

                self.printRoutes_dfs(nei, destination, curr_path, all_paths, curr_path_set)

                curr_path.pop()
                curr_path_set.remove(nei)



inst = AirportRoutes()
inst.addRoute("A", "B")
inst.addRoute("A", "C")
inst.addRoute("B", "D")
inst.addRoute("C", "D")

inst.printRoutes("A", "D")