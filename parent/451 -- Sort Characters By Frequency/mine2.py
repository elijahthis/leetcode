import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted(s)

        freq_table = []     #[[num, freq]]

        for ch in s:
            if not freq_table or freq_table[-1][0] != ch:
                freq_table.append([ch, 1])
            else:
                freq_table[-1][1] += 1
            
        
        freq_table.sort(reverse=True, key = lambda x: x[1])

        return "".join([ch[0]*ch[1] for ch in freq_table])