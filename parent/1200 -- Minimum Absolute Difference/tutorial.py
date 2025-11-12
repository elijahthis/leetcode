class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Much faster. Just one loop

        # Time: O(nlogn)
        # Space: O(n)

        arr.sort()
        ans = []
        minDiff = float("inf")

        for i in range(len(arr)-1):
            diff = abs(arr[i+1] - arr[i])
            if diff < minDiff:
                minDiff = diff
                ans = [[arr[i], arr[i+1]]]
            elif diff == minDiff:
                ans.append([arr[i], arr[i+1]])
    
        return ans