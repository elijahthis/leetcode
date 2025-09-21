class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ANALYSIS:
        # - We can use a hash map to keep track of the indexes of numbers
        # - We can iterate through the numbers and check if the complement is in the hash map
        # - If the complement is in the hash map, then we can return the indexes
        # - The time complexity is O(n) where n is the number of numbers
        # - The space complexity is O(n) where n is the number of numbers because we are using hash maps
        
        hash = {} # num -> [index]

        for i, n in enumerate(nums):
            hash.setdefault(n, [])
            hash[n].append(i)

        for i, n in enumerate(nums):
            temp_ind = hash[n][0]
            hash[n] = hash[n][1:]
            if len(hash[n]) == 0:
                hash.pop(n)

            rem = target - n
            
            if rem in hash:
                print((n, rem))
                return [i, hash[rem][0]]
            else:
                if n in hash:
                    hash[n].insert(0, temp_ind)
                else:
                    hash[n] = [temp_ind]


