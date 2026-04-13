class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sorting + two pointers pattern
        # Greedy
        # Time: O(nlogn+mlogm)
        # Space: O(1) aux.
        # Same as #455

        players.sort()
        trainers.sort()
        
        i = j = 0

        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                i += 1
            j += 1

        return i