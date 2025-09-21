class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minDiff = float("inf")

        for i, num in enumerate(arr[1:]):
            minDiff = min(minDiff, abs(arr[i] - num))
            ans.append([arr[i], num])
        
        full_ans = []
        for interval in ans:
            if abs(interval[0] - interval[1]) == minDiff:
                full_ans.append(interval)

        
        return full_ans