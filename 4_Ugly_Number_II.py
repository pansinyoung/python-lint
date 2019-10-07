"""
4. Ugly Number II
Ugly number is a number that only have prime factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Example
Example 1:

Input: 9
Output: 10
Example 2:

Input: 1
Output: 1
Challenge
O(n log n) or O(n) time.

Notice
Note that 1 is typically treated as an ugly number.
"""
import heapq


class Solution:
    def nthUglyNumber(self, n):
        heap = [1]
        visited = {1}

        for i in range(n):
            val = heapq.heappop(heap)
            for j in [2, 3, 5]:
                heapq.heappush(heap, val * j)
                visited.add(val * j)
        return val
