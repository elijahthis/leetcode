# class Node:
#     def __init__(self, cost):
#         self.cost = cost
#         self.children = []

def getMinCost(root):
    if root is None:
        return 0

    minCost = float("inf")

    def dfs(node, cost):
        nonlocal minCost
        # If leaf node, update minimum cost
        if not node.children:
            minCost = min(minCost, cost + node.val)
            return
        
        # Traverse children
        for child in node.children:
            dfs(child, cost + node.val)

    dfs(root, 0)
    return minCost


# def getMinCost(root):
#     if not root:
#         return 0

#     # Leaf node
#     if not root.children:
#         return root.cost

#     # Compute minimum cost among children
#     min_child_cost = float('inf')
#     for child in root.children:
#         min_child_cost = min(min_child_cost, getMinCost(child))
    
#     return root.cost + min_child_cost

