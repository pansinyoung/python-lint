"""
612. K Closest Points
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.

Example
Example 1:

Input: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
Output: [[1,1],[2,5],[4,4]]
Example 2:

Input: points = [[0,0],[0,9]], origin = [3, 1], k = 1
Output: [[0,0]]
"""

"""
Definition for a point.
"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


import heapq


class Solution:
    def kClosest(self, points, origin, k):
        heap = []
        for p in points:
            dist = (p.x - origin.x) ** 2 + (p.y - origin.y) ** 2
            if len(heap) == k:
                heapq.heappushpop(heap, (-dist, -p.x, -p.y))
            else:
                heapq.heappush(heap, (-dist, -p.x, -p.y))
        result = []
        while heap:
            cur = heapq.heappop(heap)
            result.append(Point(-cur[1], -cur[2]))
        result.reverse()
        return result
