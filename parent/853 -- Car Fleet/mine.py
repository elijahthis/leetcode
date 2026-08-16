class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        n = len(position)
        newArr = sorted([(position[i], speed[i]) for i in range(n)])
        res = 1

        eta = (target-newArr[n-1][0]) / newArr[n-1][1]
        for i in range(n-2, -1, -1):
            curr_eta = (target-newArr[i][0]) / newArr[i][1]
            if curr_eta <= eta:
                continue

            eta = curr_eta
            res += 1
        
        return res