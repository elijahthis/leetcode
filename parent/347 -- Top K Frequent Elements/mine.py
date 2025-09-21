class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ANALYSIS:
        # 1. Sort the list of numbers
        # 2. Create a frequency table
        # 3. Sort the frequency table by frequency
        # 4. Return the top k elements
        # Time complexity: O(nlog(n))
        # Space complexity: O(n)
        
        nums.sort()

        freq_table = []     #[[num, freq]]

        for num in nums:
            if not freq_table or freq_table[-1][0] != num:
                freq_table.append([num, 1])
            else:
                freq_table[-1][1] += 1
            
        
        freq_table.sort(reverse=True, key = lambda x: x[1])

        return [num[0] for num in freq_table[:k]]