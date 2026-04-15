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
            pos = rank[i][pair_map[i]]
            for j in range(n):
                if i != j and rank[i][j] < pos:         # all js that i prefers   
                    jMatch = pair_map[j]
                    if rank[j][i] < rank[j][jMatch]:    # does j prefer i
                        res += 1
                        break

        return res