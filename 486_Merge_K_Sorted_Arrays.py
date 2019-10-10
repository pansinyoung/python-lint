"""
486. Merge K Sorted Arrays
Given k sorted integer arrays, merge them into one sorted array.

Example
Example 1:

Input:
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Example 2:

Input:
  [
    [1,2,3],
    [1,2]
  ]
Output: [1,1,2,2,3]
Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.
"""
import heapq


class Solution:
    def mergekSortedArrays(self, arrays):
        k = len(arrays)
        heap = []
        indexes = [0 * k]
        for i in range(k):
            if arrays[i]:
                heapq.heappush(heap, (arrays[i][0], i))
        result = []
        while heap:
            cur = heapq.heappop(heap)
            result.append(cur[0])
            indexes[cur[1]] += 1
            if indexes[cur[1]] < len(arrays[cur[1]]):
                heapq.heappush(heap, (arrays[cur[1]][indexes[cur[1]]], cur[1]))
        return result


