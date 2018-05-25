import collections

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}

        self.size = 0
        self.capacity = capacity

        self.head = None
        self.tail = None


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1

        node = self.dict[key]
        self._remove_node(node)
        self._add_head(node)

        return self.dict[key].value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # new element is considered as recently used


        if key in self.dict:
            node = self.dict[key]
            self._remove_node(node)
            node.value = value
        else:
            node = Node(key, value)
            if self.size >= self.capacity:
                del_key = self._remove_last()
                del self.dict[del_key]

        self._add_head(node)
        self.dict[key] = node

    def _add_head(self, node):
        node.prev = None

        if self.size == 0:
            node.next = None
            self.tail = node
        elif self.size >= 1:
            node.next = self.head
            self.head.prev = node

        self.head = node
        self.size += 1


    def _remove_node(self, node):
        if node is None or self.size == 0:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            self.head.prev = None
        elif self.tail is node:
            self._remove_last()
            self.size += 1
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

    def _remove_last(self):
        if self.size == 0:
            return

        key = self.tail.key

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

        return key

class LRUCacheDict:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        # FIFO operation
        try:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            print(self.cache.popitem(last=False))






#cache = LRUCache(2)
cache = LRUCacheDict(2)

cache.put(2,1)
cache.put(1,1)
cache.put(2,3)
cache.put(4,1)
print(cache.get(1))
print(cache.get(2))
'''
cache.put(1, 1)

cache.put(2, 2)

print(cache.get(1))       # returns 1

cache.put(3, 3)    # evicts key 2

print(cache.get(2))       # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1))       # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))       # returns 4
'''
