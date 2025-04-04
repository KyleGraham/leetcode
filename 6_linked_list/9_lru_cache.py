

#solution using doubly linked list
#time complexity O(1) for each put() and get() operation
#space complexity O(n)

#uses a hash to keep track of the current key and values in the linked list
#uses a doubly linked list to keep track of the order of the keys
#most of this problem is just remembeing how to implement the different doubly linked list operations
# the get checks if the key is in the cache, if it is, it removes the node from the linked list and inserts it at the end of the linked list
# the put checks if the key is in the cache, if it is, it removes the node from the linked list
# then it inserts the node at the end of the linked list
# if the list is too long now, it removes the value at the start of the list and removes it from the cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
#solution using OrderedDict from collections built in python data structure 
# much cleaner solution IMO

#get just checks if key is in the cache, returns -1 if not
# if key is in cache, it moves the key to the end of the ordered dictionary
#returns the value of the key

#put checks if the key is in the cache
# if it is, it moves the key to the end of the ordered dictionary
# if the cache is too long, it removes the first key in the ordered dictionary
            
class LRUCache:
  
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)