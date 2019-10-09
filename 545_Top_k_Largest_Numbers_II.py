"""
545. Top k Largest Numbers II
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
Example
Example1

Input:
s = new Solution(3);
s.add(3)
s.add(10)
s.topk()
s.add(1000)
s.add(-99)
s.topk()
s.add(4)
s.topk()
s.add(100)
s.topk()

Output:
[10, 3]
[1000, 10, 3]
[1000, 10, 4]
[1000, 100, 10]

Explanation:
s = new Solution(3);
>> create a new data structure, and k = 3.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
Example2

Input:
s = new Solution(1);
s.add(3)
s.add(10)
s.topk()
s.topk()

Output:
[10]
[10]

Explanation:
s = new Solution(1);
>> create a new data structure, and k = 1.
s.add(3)
s.add(10)
s.topk()
>> return [10]
s.topk()
>> return [10]
"""
import heapq



class Solution:
    def __init__(self, k):
        self.data = []
        self.capacity = k

    def add(self, num):
        if len(self.data) == self.capacity:
            heapq.heappushpop(self.data, num)
        else:
            heapq.heappush(self.data, num)

    def topk(self):
        return heapq.nlargest(self.capacity, self.data)
