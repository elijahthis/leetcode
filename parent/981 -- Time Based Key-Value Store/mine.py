from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # Time: O(logn)         Optimal could be cleaner
        # Space: O(1)
        if not self.store[key]:
            return ""

        l, r = 0, len(self.store[key])-1
        
        while l <= r:
            if r-l < 2:
                if timestamp < self.store[key][l][1]:
                    return ""
                elif timestamp < self.store[key][r][1]:
                    return self.store[key][l][0]
                else:
                    return self.store[key][r][0]
            
            mid = (l+r) // 2
            if self.store[key][mid][1] <= timestamp:
                l = mid
            else:
                r = mid
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)