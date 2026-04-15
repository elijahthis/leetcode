class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Greedy. Optimal.
        # Time: O(n log n)
        # Space: O(1) aux.
        # fractional Knapsack-style greedy problem

        boxTypes.sort(key=lambda x: -x[1])
        res = currSize = 0

        for num, units in boxTypes:
            if currSize < truckSize:
                res += (units * min(num, truckSize-currSize))
                currSize += min(num, truckSize-currSize)
        
        return res