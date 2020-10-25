import heapq
import unittest


class LRUCache:
    """
    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
    operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
    it should invalidate the least recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

    Follow up:
    Could you do both operations in O(1) time complexity?

    Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Internal data             # Item: (usage, (key, value))
        self.item_table = {}  # {key: (usage, (key, value))}
        self.black_list = set()  # set((usage, (key, value)))
        self.heap = []  # heap([(usage, (key, value))])

        self.usage_step = 0

    def get(self, key: int) -> int:
        if key in self.item_table:
            return self.update_existing_item_and_return_value(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.item_table:
            self.update_existing_item_and_return_value(key, value)
        else:
            if len(self.item_table) < self.capacity:
                self.add_new_item(key, value)
            else:
                while self.heap:
                    popped_item = heapq.heappop(self.heap)
                    if popped_item in self.black_list:
                        self.black_list.remove(popped_item)
                        continue
                    else:
                        usage, (old_key, old_value) = popped_item
                        del self.item_table[old_key]
                        break
                self.add_new_item(key, value)

    def add_new_item(self, key, value):
        self.usage_step += 1
        item = (self.usage_step, (key, value))
        self.item_table[key] = item
        heapq.heappush(self.heap, item)

    def update_existing_item_and_return_value(self, key, new_value=None) -> int:
        # Increment current usage
        self.usage_step += 1
        usage, (_, value) = self.item_table[key]

        # Update value if new one will be inserted
        new_item = self.usage_step, (key, new_value if new_value is not None else value)
        self.item_table[key] = new_item
        self.black_list.add((usage, (key, value)))
        heapq.heappush(self.heap, new_item)
        return value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCacheTest(unittest.TestCase):

    def test_case_1(self):
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(1, cache.get(1))
        cache.put(3, 3)
        self.assertEqual(-1, cache.get(2))
        cache.put(4, 4)
        self.assertEqual(-1, cache.get(1))
        self.assertEqual(3, cache.get(3))
        self.assertEqual(4, cache.get(4))

    def test_case_2(self):
        cache = LRUCache(2)
        cache.put(2, 1)
        cache.put(2, 2)
        self.assertEqual(2, cache.get(2))
        cache.put(1, 1)
        cache.put(4, 1)
        self.assertEqual(-1, cache.get(2))
