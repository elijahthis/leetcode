class Solution:
    def findDaysS2SubsequenceOfS1(self, s1, s2, start, end) -> int:
        currS1 = s1
        count = 0
        for ind in range(len(start)):
            # currS1 = currS1[start[ind] : end[ind]]
            currS1 = s1[:start[ind]] + s1[end[ind]+1:]
            # print('currS1: ' + currS1)
            if s2 in currS1:
                count += 1



inst = Solution()

inst.findDaysS2SubsequenceOfS1('abcdefghabc', 'abc', [0, 0, 1, 2, 9], [1, 2, 3, 3, 10])