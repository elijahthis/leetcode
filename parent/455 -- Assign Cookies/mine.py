class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sorting + two pointers pattern
        # Greedy
        # Time: O(nlogn+mlogm)
        # Space: O(1) aux.
        # Same as #2410
        
        g.sort()
        s.sort()

        res = 0
        cookie = 0
        
        for child in g:
            while cookie < len(s) and s[cookie] < child:
                cookie += 1
            if cookie == len(s):
                break
            
            res += 1
            cookie += 1
        
        return res
            