from typing import List

class Solution:
  def getMaximumSum(self, data: List[List[int]], factor: List[int], x: int) -> int:
    tempData = data
    tempLargeStore = []
    for i in range(len(factor)):
      tempData[i].sort()
      smallArr = tempData[i][-factor[i]:]
      tempLargeStore = [*tempLargeStore, *smallArr]
    tempLargeStore.sort()
    print('tempLargeStore: ' + str(tempLargeStore))
    print('result: ' + str(sum(tempLargeStore[-x:])))
    return sum(tempLargeStore[-x:])


inst = Solution()
inst.getMaximumSum([[1, 2, 3], [8,7,6], [7, 8, 9]], [1, 2, 3], 2)