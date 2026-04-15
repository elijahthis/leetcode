class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Hint: 
        # Converts preference lists into O(1) lookup tables
        # Time: O(n^2)
        # Space: O(n^2). Mostly rank
        
        rank = []   # rank[i][j] = position of j in i’s preference list
        pair_map = [0]*n
        res = 0
        
        for i in range(n):
            obj = {}
            for j in range(n-1):
                obj[preferences[i][j]] = j+1    # Lower value = more preferred
            rank.append(obj)
        
        for u,v in pairs:
            pair_map[u] = v
            pair_map[v] = u

        for i in range(n):
            partner = pair_map[i]
            # Insight:
            # Preferences are already sorted by preference
            # You only scan until current partner
            # Avoids unnecessary checks
            for j in preferences[i]:
                if j == partner:
                    break
                
                if rank[j][i] < rank[j][pair_map[j]]:
                    res += 1
                    break

        return res