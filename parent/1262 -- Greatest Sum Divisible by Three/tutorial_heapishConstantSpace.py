import heapq
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        smallest_one = float("inf")
        smallest_two = float("inf")
        totalSum = 0

        for n in nums:
            totalSum += n
            if n%3 == 1:
                smallest_two = min(smallest_two, smallest_one + n) 
                smallest_one = min(smallest_one, n)
            elif n%3 == 2:
                smallest_one = min(smallest_one, smallest_two + n)  
                smallest_two = min(smallest_two, n)
        
        if totalSum%3 == 1:
            return totalSum - smallest_one
        elif totalSum%3 == 2:
            return totalSum - smallest_two
        else:
            return totalSum

