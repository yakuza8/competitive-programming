from collections import defaultdict
from math import inf


class AllOne:
    """
    Implement a data structure supporting the following operations:

    * Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty
    string.
    * Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1.
    If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
    * GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
    * GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

    Challenge: Perform all these in O(1) time complexity.

    Runtime: 84 ms, faster than 78.72% of Python3 online submissions for All O`one Data Structure.
    Memory Usage: 20.4 MB, less than 50.00% of Python3 online submissions for All O`one Data Structure.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container_value = defaultdict(int)
        self.values = defaultdict(dict)
        self.max_key = -inf
        self.min_key = inf

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        current_value = self.container_value[key]
        new_value = current_value + 1
        self.replace_key_with_new_value(key, current_value, new_value)
        self.update_min_max(new_value)

        if current_value == self.min_key and len(self.values[current_value]) == 0:
            self.min_key = new_value

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.container_value:
            return

        current_value = self.container_value[key]
        new_value = current_value - 1
        self.replace_key_with_new_value(key, current_value, new_value, True)
        self.update_min_max(new_value)

        if current_value == self.max_key and len(self.values[current_value]) == 0:
            self.max_key = new_value

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.max_key == -inf:
            return ""

        return next(iter(self.values[self.max_key].keys()))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.min_key == inf:
            return ""

        return next(iter(self.values[self.min_key].keys()))

    def replace_key_with_new_value(self, key: str, current_value: int, new_value: int, removal: bool = False) -> None:
        # Remove from the priority queue
        if key in self.values[current_value]:
            del self.values[current_value][key]

        if current_value == 1 and removal:
            del self.container_value[key]
            return

        self.container_value[key] = new_value
        self.values[new_value][key] = False

    def update_min_max(self, new_value: int) -> None:
        # Update max value
        if new_value > self.max_key:
            self.max_key = new_value
        if new_value != 0 and new_value < self.min_key:
            self.min_key = new_value
        else:
            if len(self.container_value.values()) == 0:
                self.min_key = inf
                self.max_key = -inf
            else:
                self.min_key = min(self.container_value.values())


structure = AllOne()
s1 = "berat"
structure.inc(s1)
structure.inc(s1)
print()
s2 = "tulin"
structure.inc(s2)
structure.inc(s2)
structure.inc(s1)
structure.inc(s2)
structure.inc(s2)
print()

structure.dec(s1)
structure.dec(s1)
structure.dec(s1)
structure.dec(s1)
print()

structure.dec(s2)
structure.dec(s2)
structure.dec(s2)
structure.dec(s2)