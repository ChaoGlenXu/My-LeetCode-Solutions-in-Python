#146. LRU Cache
#Medium
#problem statement:    https://leetcode.com/problems/lru-cache/description/

class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.nxt = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity    
        self.cache = {}     
        #self.queue = {}
        self.l = Node(0, 0) #most left LRu
        self.r = Node(0, 0) #most recent 
        self.l.nxt, self.r.prev = self.r, self.l

    def remove(self, node: Node) -> Node:
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        return node

    def insert(self, node: Node): #to the most right
        prev, nxt = self.r.prev, self.r
        
        prev.nxt = nxt.prev = node

        node.prev, node.nxt = prev, nxt
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.remove(self.cache[key])
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) 

        if len(self.cache) >  self.cap: 
            lru = self.l.nxt
            self.remove(lru)
            del self.cache[lru.key]
        return None
        


            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
