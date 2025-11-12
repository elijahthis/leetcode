class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # If x[0] - x[1] is small or negative, it's cheaper (or better) to send to city A.
        # If it's large or positive, it’s cheaper to send to city B.

        costs.sort(key=lambda x:x[0]-x[1])
        mid = len(costs)//2
        city_a = sum(x[0] for x in costs[:mid])
        city_b = sum(x[1] for x in costs[mid:])
        return city_a + city_b
        