class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sorting + two pointers pattern
        # Greedy
        # Time: O(nlogn+mlogm)
        # Space: O(1) aux.
        # Same as #455

        players.sort()
        trainers.sort()

        t = 0
        res = 0
        
        for p in players:
            while t < len(trainers) and p > trainers[t]:
                t += 1
            if t == len(trainers):
                break
            
            res += 1
            t += 1
        
        return res