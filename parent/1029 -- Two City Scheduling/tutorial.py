class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # ANALYSIS:
        # - We can sort the costs by the difference between the cost of going to city A and city B
        # - We can then iterate through the sorted costs and send the first half of the people to city A and the second half of the people to city B
        # - The time complexity is O(nlogn) where n is the number of people
        # - The space complexity is O(n) where n is the number of people
        # GREEDY ALGORITHM

        diff_arr = []      # [[diff, originalArr]]
        total = 0

        for person in costs:
            diff_arr.append([person[1] - person[0], person])

        diff_arr.sort(key = lambda x: x[0])
        
        for i, person in enumerate(diff_arr):
            if i < len(diff_arr) / 2:
                total += person[1][1]
            else:
                total += person[1][0]
                
        return total