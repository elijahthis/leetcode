# Definition for a Sea.
# class Sea:
#     def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#         pass

# Definition for a Point.
# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y



# Divide and conquer
# Time: O(S log A)
# Space: O(log A) — recursion depth.
# S = number of ships,
# A = area of the search region.
class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # Base case: invalid region
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        
        # If no ship in this region
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # Base case: region is a single point, and hasShips confirmed True
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return 1
        
        # Divide rectangle into 4 smaller parts
        midX = (bottomLeft.x + topRight.x) // 2
        midY = (bottomLeft.y + topRight.y) // 2

        topLeftQ = dfs(Point(midX, y2), Point(x1, midY+1))
        topRightQ = dfs(Point(x2, y2), Point(midX+1,midY+1))
        bottomLeftQ = dfs(Point(midX, midY), Point(x1,y1))
        bottomRightQ = dfs(Point(x2, midY), Point(midX+1, y1))

        return topLeftQ + topRightQ + bottomLeftQ + bottomRightQ
