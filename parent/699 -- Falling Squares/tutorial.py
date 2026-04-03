class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # brute-force Line sweep passes well
        # Time: O(n^2)
        # Space: O(n)
        intervals = []      # [[l,r,h]]
        heights = []        # result

        for left, size in positions:
            right = left + size
            maxHeight = 0

            # find maxHeight by adding overlaps
            for l,r,h in intervals:
                if not (l >= right or r <= left):
                    maxHeight = max(maxHeight, h)
            
            currHeight = maxHeight + size
            intervals.append((left, right, currHeight))
            heights.append(currHeight if not heights else max(currHeight, heights[-1]))
        
        return heights