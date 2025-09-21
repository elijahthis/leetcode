import random

class RandomizedSet:
    # pretty straight-forward.
    # Key Points:
    #  1. Use a hashset to store the elements. This will help in O(1) time complexity for insert and remove operations.
    #  2. Use a list to store the elements in parallel. This will help in O(1) time complexity for getRandom operation.
    
    def __init__(self):
        self.my_set = set()
        self.my_list = []

    def insert(self, val: int) -> bool:
        if val in self.my_set:
            return False
        else:
            self.my_set.add(val)
            self.my_list.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.my_set:
            self.my_set.remove(val)
            self.my_list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        element_index = random.randrange(0, len(self.my_list))
        element = self.my_list[element_index]

        return element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()