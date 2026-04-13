class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Union Find
        # Time: O(n). Works, and technically falls under optimal, but logical overkill
        # Space: O(n)

        if not nums:
            return 0
        size = {}
        parent = {}
        nums_set = set(nums)

        for num in nums_set:
            parent[num] = num
            size[num] = 1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootX, rootY = find(parent[x]), find(parent[y])
            sizeX, sizeY = size[x], size[y]

            if rootX != rootY:
                if sizeX < sizeY:
                    rootX, rootY = rootY, rootX
                    sizeX, sizeY = sizeY, sizeX
                
                parent[rootY] = rootX
                size[rootX] += size[rootY]
        
        # Union consecutive numbers
        for num in nums_set:
            if num+1 in nums_set:
                union(num, num+1)
        
        return max(size[find(x)] for x in nums_set)

