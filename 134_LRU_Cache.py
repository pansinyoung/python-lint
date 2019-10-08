"""
134. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
Finally, you need to return the data from each get.

Example
Example1

Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation：
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
Example 2:

Input：
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output：[1,-1,2]
Explanation：
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
"""
import heapq


class LinkedNode:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next



class LRUCache:
    def __init__(self, capacity):
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity
        self.map_to_prev = {}

    def kick_to_back(self, node):
        if node == self.tail:
            return
        self.map_to_prev[node.key].next = node.next
        self.map_to_prev[node.next.key] = self.map_to_prev[node.key]
        node.next = None
        self.tail.next = node
        self.map_to_prev[node.key] = self.tail
        self.tail = node

    def get(self, key):
        if key not in self.map_to_prev:
            return -1
        self.kick_to_back(self.map_to_prev[key].next)
        return self.map_to_prev[key].next.value

    def set(self, key, value):
        if key in self.map_to_prev:
            self.map_to_prev[key].next.value = value
            self.kick_to_back(self.map_to_prev[key].next)
            return
        node = LinkedNode(key, value)
        self.map_to_prev[key] = self.tail
        self.tail.next = node
        self.tail = node
        if len(self.map_to_prev) > self.capacity:
            cur = self.dummy.next
            self.dummy.next = cur.next
            self.map_to_prev[self.dummy.next.key] = self.dummy
            cur.next = None
            del self.map_to_prev[cur.key]
