from typing import Dict


class LRUCache(object):

    def __init__(self, capacity: int) -> None:
        self.ages: Dict[int, int] = {}
        self.cache: Dict[int, int] = {}
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        # Retrieve item from provided key. Return -1 if nonexistent.
        ret = self.cache.get(key, -1)
        if ret == -1:
            return ret
        age = self.ages[key]
        for k, v in self.ages.items():
            if v < age:
                self.ages[k] += 1
            elif v == age:
                self.ages[k] = 0
        return ret

    def set(self, key: int, value: int) -> None:
        # Set the value if the key is not present in the cache. If the cache is
        # at capacity remove the oldest item.
        if self.capacity == 0:
            return
        # for simplicity overwriting a value is a silently ignored error
        if key in self.cache:
            return
        del_k = None
        for k, v in self.ages.items():
            if v == self.capacity - 1:
                del_k = k
            else:
                self.ages[k] += 1
        if del_k is not None:
            del self.ages[del_k]
            del self.cache[del_k]
        self.ages[key] = 0
        self.cache[key] = value


our_cache: LRUCache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
# TODO: I got stuck here, because in O(1) I can only either get something from
# one end of a list (i.e. queue/stack) or get something from a hash, but that
# doesn't seem to be enough to take the 2 from the middle of my queue to the
# beginning.
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached its capacity and 3 was the least
# recently used entry
print(our_cache.get(3))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large
# values

# Test Case 1
empty_cache: LRUCache = LRUCache(0)
print(empty_cache.get(42))  # returns -1

# Test Case 2
empty_cache = LRUCache(0)
empty_cache.set(1, 1)
print(empty_cache.get(1))  # returns -1

# Test Case 3
two_cache: LRUCache = LRUCache(2)
two_cache.set(1, 1)
two_cache.set(2, 2)
two_cache.set(3, 3)
two_cache.set(4, 4)
print(two_cache.get(1))  # returns -1
print(two_cache.get(2))  # returns -1
print(two_cache.get(3))  # returns 3
print(two_cache.get(4))  # returns 4
