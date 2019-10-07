"""
544. Top k Largest Numbers
Given an integer array, find the top k largest numbers in it.

Example
Example1

Input: [3, 10, 1000, -99, 4, 100] and k = 3
Output: [1000, 100, 10]
Example2

Input: [8, 7, 6, 5, 4, 3, 2, 1] and k = 5
Output: [8, 7, 6, 5, 4]
"""


import heapq


class Solution:
    def topk(self, nums, k):
        heap = []
        for n in nums:
            if len(heap) == k:
                heapq.heappushpop(heap, -n)
            else:
                heapq.heappush(heap, -n)

        result = []
        while heap:
            result.append(heapq.heappop(heap))
        result.reverse()
        return result
