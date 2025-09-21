class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    # ANALYSIS
    # Time Complexity: O(1) for both get and put
    # Space Complexity: O(capacity) for cache and O(1) for left and right
    # We use a doubly linked list to keep track of the order of the keys
    # We use a dictionary (hashmap) to store the key -> node mapping
    # We use a dummy head and tail to avoid edge cases when removing or inserting nodes
    # We remove the least recently used node from the left of the list
    # We insert the most recently used node at the right of the list


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}     # key -> node
        
        # left - LRU, right -> MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from linked list
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # insert node at rightmost of linked list
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        # if key exists, remove it and insert it at right
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, remove it and insert it at right
        # update value
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if capacity is full, remove LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
          

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)