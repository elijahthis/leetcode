import heapq

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        rem1 = []
        rem2 = []
        total = sum(nums)

        for n in nums:
            if n % 3 == 1:
                heapq.heappush(rem1, -n)
                if len(rem1) > 2:
                    heapq.heappop(rem1)
            elif n % 3 == 2:
                heapq.heappush(rem2, -n)
                if len(rem2) > 2:
                    heapq.heappop(rem2)

        # Convert to sorted smallest-values array
        r1 = sorted(-x for x in rem1)
        r2 = sorted(-x for x in rem2)

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            cand1 = r1[0] if len(r1) > 0 else float('inf')
            cand2 = (r2[0] + r2[1]) if len(r2) > 1 else float('inf')
            return total - min(cand1, cand2)

        # total % 3 == 2
        cand1 = r2[0] if len(r2) > 0 else float('inf')
        cand2 = (r1[0] + r1[1]) if len(r1) > 1 else float('inf')
        return total - min(cand1, cand2)
