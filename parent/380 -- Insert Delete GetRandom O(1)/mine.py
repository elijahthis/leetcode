import random

class RandomizedSet:
    # pretty straight-forward.
    
    def __init__(self):
        self.my_hash = {}
        self.my_list = []

    def insert(self, val: int) -> bool:
        if val in self.my_hash:
            return False
        self.my_hash[val] = len(self.my_hash)
        self.my_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.my_hash:
            return False

        lastVal, ind = self.my_list[-1], self.my_hash[val]
        self.my_list[ind] = lastVal
        self.my_hash[lastVal] = ind
        
        self.my_list.pop()
        del self.my_hash[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.my_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()